import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import random
import math


array = random.sample(range(1, 1000), 100)
sorted_array = sorted(array)


fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(sorted_array)), sorted_array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(checked, found):
    for i, bar in enumerate(bars):
        bar.set_color("red" if i in checked else "lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {checked[-1]}")
    else:
        title.set_text(f"Jump Search - Checked indices: {checked}")

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < x:
        yield list(range(prev, min(step, n)))
        prev = step
        step += int(math.sqrt(n))
    for i in range(prev, min(step, n)):
        yield [i]
        if arr[i] == x:
            return i
    return -1


value_to_search = random.choice(sorted_array)
print(f"Value to search: {value_to_search}")


search_gen = jump_search(sorted_array, value_to_search)


steps = 0
found_index = -1


pause_interval = 0.2  


while True:
    try:
        checked = next(search_gen)
        if sorted_array[checked[-1]] == value_to_search:
            found_index = checked[-1]
            update_bars(checked, True)
            title.set_text(f"Value {value_to_search} found at index {found_index} after {steps} steps")
            print(f"Value found at index: {found_index}")
            print(f"Total steps taken: {steps}")
            print("Time Complexity: O(√n)")
            print("Space Complexity: O(1)")
            plt.draw()  
            plt.pause(2)  
            plt.close()  
            break
        else:
            update_bars(checked, False)
            plt.draw()  
            plt.pause(pause_interval)  
            steps += 1
    except StopIteration:
        
        if found_index == -1:
            update_bars(range(len(sorted_array)), False)
            title.set_text(f"Value {value_to_search} not found after {steps} steps")
            print(f"Value not found after {steps} steps")
            plt.draw()  
            plt.pause(7)  
            plt.close()  
        break
