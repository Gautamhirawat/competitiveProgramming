import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import random


def ternary_search(arr, left, right, x, steps):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        steps.append(mid1)
        steps.append(mid2)

        if arr[mid1] == x:
            return mid1, steps
        if arr[mid2] == x:
            return mid2, steps

        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x, steps)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x, steps)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x, steps)

    return -1, steps


array = sorted(random.sample(range(1, 1000), 100))


fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(array)), array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(index, found):
    for i, bar in enumerate(bars):
        bar.set_color("red" if i == index else "lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {index}")
    else:
        title.set_text(f"Ternary Search - Checking index: {index}")


value_to_search = random.choice(array)
print(f"Value to search: {value_to_search}")


steps = []
index, search_steps = ternary_search(array, 0, len(array) - 1, value_to_search, steps)


if index != -1:
    update_bars(index, True)
    title.set_text(f"Value {value_to_search} found at index {index} after {len(search_steps)} steps")
    print(f"Value found at index: {index}")
    print(f"Total steps taken: {len(search_steps)}")
else:
    update_bars(len(array) - 1, False)
    title.set_text(f"Value {value_to_search} not found after {len(search_steps)} steps")
    print(f"Value not found after {len(search_steps)} steps")

plt.draw()
plt.pause(7)
plt.close()
