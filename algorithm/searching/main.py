import os
import pandas as pd
from tabulate import tabulate

def run_algorithm(algorithm_name):
    script_map = {
        "linear": "linear_search.py",
        "binary": "binary_search.py",
        "jump": "jump_search.py",
        "exponential": "exponential_search.py",
        "hashing": "hashing_search.py",
        "best_first": "best_first_search.py",
        "dfs": "dfs_search.py",
        "bfs": "bfs_search.py",
        "fibonacci": "fibonacci_search.py",
        "ternary": "ternary_search.py",
        "interpolation": "interpolation_search.py",
    }
    
    script_name = script_map.get(algorithm_name.lower())
    if script_name and os.path.isfile(script_name):
        os.system(f"python3 {script_name} > temp_output.txt")
    else:
        print(f"Script for {algorithm_name} not found.")

def run_all_algorithms():
    algorithms = [
        "linear", "binary", "jump", "exponential", "hashing", 
        "best_first", "dfs", "bfs", "fibonacci", "ternary", 
        "interpolation"
    ]
    
    results = []
    
    for algo in algorithms:
        print(f"Running {algo.replace('_', ' ').title()}...")
        run_algorithm(algo)
        
        with open("temp_output.txt", "r") as file:
            output = file.readlines()
        
        
        print(f"\nOutput for {algo}:")
        print("".join(output))
        

        value = found_index = steps = time_complexity = space_complexity = "N/A"
        
        if len(output) >= 5:
            try:
                value = output[0].strip().split(": ")[1]
                found_index = output[1].strip().split(": ")[1]
                steps = output[2].strip().split(": ")[1]
                time_complexity = output[3].strip().split(": ")[1]
                space_complexity = output[4].strip().split(": ")[1]
            except IndexError:
                print(f"Error parsing output for {algo}. Check the output format.")
        
        results.append({
            "Algorithm": algo.replace('_', ' ').title(),
            "Value to Search": value,
            "Value Found at Index": found_index,
            "Total Steps Taken": steps,
            "Time Complexity": time_complexity,
            "Space Complexity": space_complexity
        })
    
    df = pd.DataFrame(results)
    df_sorted = df.sort_values(by="Total Steps Taken")
    
    print("\nSummary of All Algorithms:")
    print(tabulate(df_sorted, headers='keys', tablefmt='pretty'))
    
    
    df_sorted.to_csv("search_summary.csv", index=False)

def main():
    while True:
        print("Choose a search algorithm to run:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Jump Search")
        print("4. Exponential Search")
        print("5. Hashing Search")
        print("6. Best-First Search")
        print("7. Depth-First Search (DFS)")
        print("8. Breadth-First Search (BFS)")
        print("9. Fibonacci Search")
        print("10. Ternary Search")
        print("11. Interpolation Search")
        print("12. Run All Algorithms")
        print("13. Exit")
        
        choice = input("Enter your choice (1-13): ")
        
        algorithms = {
            "1": "linear",
            "2": "binary",
            "3": "jump",
            "4": "exponential",
            "5": "hashing",
            "6": "best_first",
            "7": "dfs",
            "8": "bfs",
            "9": "fibonacci",
            "10": "ternary",
            "11": "interpolation",
        }
        
        if choice == "12":
            run_all_algorithms()
        elif choice == "13":
            print("Exiting...")
            break
        else:
            algorithm_name = algorithms.get(choice)
            if algorithm_name:
                run_algorithm(algorithm_name)
            else:
                print("Invalid choice. Please select a number between 1 and 13.")

if __name__ == "__main__":
    main()
