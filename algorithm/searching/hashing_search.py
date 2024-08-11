import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import random


array = random.sample(range(1, 1000), 100)
sorted_array = sorted(array)


hash_table = {value: index for index, value in enumerate(sorted_array)}


fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(sorted_array)), sorted_array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(index, found):
    for i, bar in enumerate(bars):
        bar.set_color("red" if i == index else "lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {index}")
    else:
        title.set_text(f"Hashing Search - Searching...")

def hashing_search(arr, hash_table, x):
    if x in hash_table:
        yield hash_table[x]
        return hash_table[x]
    return -1


value_to_search = random.choice(sorted_array)
print(f"Value to search: {value_to_search}")


search_gen = hashing_search(sorted_array, hash_table, value_to_search)


steps = 0
found_index = -1


pause_interval = 0.1  


try:
    found_index = next(search_gen)
    update_bars(found_index, True)
    title.set_text(f"Value {value_to_search} found at index {found_index}")
    print(f"Value found at index: {found_index}")
    print(f"Total steps taken: {steps}")
    print("Time Complexity: O(1)")
    print("Space Complexity: O(n)")
    plt.draw()  
    plt.pause(2)  
    plt.close()  
except StopIteration:
    
    update_bars(len(sorted_array) - 1, False)
    title.set_text(f"Value {value_to_search} not found")
    print(f"Value not found")
    plt.draw()  
    plt.pause(7)  
    plt.close()  
