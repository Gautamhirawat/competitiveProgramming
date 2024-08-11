import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import heapq

array = random.sample(range(1, 1000), 100)
sorted_array = sorted(array)

fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(sorted_array)), sorted_array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(index, found):
    for i, bar in enumerate(bars):
        bar.set_color("red" if i == index else "lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {index}")
    else:
        title.set_text(f"Best-First Search - Checking index: {index}")

def best_first_search(arr, x):
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0))  
    visited = set()
    while priority_queue:
        _, index = heapq.heappop(priority_queue)
        yield index
        if arr[index] == x:
            return index
        if index not in visited:
            visited.add(index)
            if index > 0:
                heapq.heappush(priority_queue, (abs(arr[index - 1] - x), index - 1))
            if index < len(arr) - 1:
                heapq.heappush(priority_queue, (abs(arr[index + 1] - x), index + 1))
    return -1

value_to_search = random.choice(sorted_array)
print(f"Value to search: {value_to_search}")


search_gen = best_first_search(sorted_array, value_to_search)

steps = 0
found_index = -1

pause_interval = 0.1  

while True:
    try:
        index = next(search_gen)
        if sorted_array[index] == value_to_search:
            found_index = index
            update_bars(index, True)
            title.set_text(f"Value {value_to_search} found at index {index} after {steps} steps")
            print(f"Value found at index: {index}")
            print(f"Total steps taken: {steps}")
            print("Time Complexity: O(n log n) on average")
            print("Space Complexity: O(n)")
            plt.draw()  
            plt.pause(2)  
            plt.close()  
            break
        else:
            update_bars(index, False)
            plt.draw()  
            plt.pause(pause_interval)  
            steps += 1
    except StopIteration:
        
        if found_index == -1:
            update_bars(len(sorted_array) - 1, False)
            title.set_text(f"Value {value_to_search} not found after {steps} steps")
            print(f"Value not found after {steps} steps")
            plt.draw()  
            plt.pause(7)  
            plt.close()  
        break
