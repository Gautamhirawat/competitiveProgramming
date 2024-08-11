import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import random


array = random.sample(range(1, 1000), 100)
sorted_array = sorted(array)


fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(sorted_array)), sorted_array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(low, high, mid, found):
    for i, bar in enumerate(bars):
        if low <= i <= high:
            bar.set_color("orange" if i == mid else "lightblue")
        else:
            bar.set_color("lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {mid}")
    else:
        title.set_text(f"Binary Search - Low: {low}, High: {high}, Mid: {mid}")

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        yield low, high, mid
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


value_to_search = random.choice(sorted_array)
print(f"Value to search: {value_to_search}")


search_gen = binary_search(sorted_array, value_to_search)


steps = 0
found_index = -1


pause_interval = 0.1  


while True:
    try:
        low, high, mid = next(search_gen)
        if sorted_array[mid] == value_to_search:
            found_index = mid
            update_bars(low, high, mid, True)
            title.set_text(f"Value {value_to_search} found at index {mid} after {steps} steps")
            print(f"Value found at index: {mid}")
            print(f"Total steps taken: {steps}")
            print("Time Complexity: O(log n)")
            print("Space Complexity: O(1)")
            plt.draw()  
            plt.pause(2)  
            plt.close()  
            break
        else:
            update_bars(low, high, mid, False)
            plt.draw()  
            plt.pause(pause_interval)  
            steps += 1
    except StopIteration:
        
        if found_index == -1:
            update_bars(0, len(sorted_array) - 1, len(sorted_array) // 2, False)
            title.set_text(f"Value {value_to_search} not found after {steps} steps")
            print(f"Value not found after {steps} steps")
            plt.draw()  
            plt.pause(7)  
            plt.close()  
        break
