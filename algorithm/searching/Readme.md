# Search Algorithms Visualization

*This project demonstrates various search algorithms by visualizing their execution. It includes scripts to run different search algorithms, record their execution, and convert the recordings into tables in form of csv files.*

## Project Structure

- `linear_search.py`: Script to perform Linear Search.
- `binary_search.py`: Script to perform Binary Search.
- `jump_search.py`: Script to perform Jump Search.
- `exponential_search.py`: Script to perform Exponential Search.
- `hashing_search.py`: Script to perform Hashing Search.
- `best_first_search.py`: Script to perform Best-First Search.
- `dfs_search.py`: Script to perform Depth-First Search (DFS).
- `bfs_search.py`: Script to perform Breadth-First Search (BFS).
- `fibonacci_search.py`: Script to perform Fibonacci Search.
- `ternary_search.py`: Script to perform Ternary Search.
- `interpolation_search.py`: Script to perform Interpolation Search.
- `record_and_convert.py`: Script to record each algorithm execution and convert it to GIF.

## Requirements

- Python 3
- `pandas` (for data handling)
- `matplotlib` (for displaying summary tables)

You can install the required Python packages using pip:

```bash
pip install pandas matplotlib
```

## How to Use

Run All Scripts Seperately or you can run main file

```bash
python3 main.py
```

Now you can run any of the above files or there is another option that can be used to run all files one after another.

## Conclusion 

- `Linear Search`: Sequentially checks each element until it finds the target or exhausts the list.
- `Binary Search`: Efficiently finds the target in a sorted list by repeatedly dividing the search interval in half.
- `Jump Search`: Jumps ahead by a fixed number of steps and then performs a linear search within the block.
- `Exponential Search`: Exponentially increases the search range and then uses binary search within the identified range.
- `Hashing Search`: Uses a hash table to provide constant time complexity for search operations.
- `Best-First Search`: Searches using a heuristic to prioritize nodes that appear to be closer to the goal.
- `Depth-First Search` (DFS): Explores as far as possible along each branch before backtracking.
- `Breadth-First Search` (BFS): Explores all neighbors at the present depth level before moving on to nodes at the next depth level.
- `Fibonacci Search`: Uses Fibonacci numbers to reduce the search range in a sorted list.
- `Ternary Search`: Divides the search interval into three parts and recursively searches in the relevant segment.
- `Interpolation Search`: Uses the value of the target to estimate its position in a sorted list and then searches around that position.

