import matplotlib
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt
import random


array = random.sample(range(1, 1000), 100)
sorted_array = sorted(array)


fig, ax = plt.subplots(figsize=(20, 20))
bars = ax.bar(range(len(sorted_array)), sorted_array, color="lightblue")
title = ax.text(0.5, 1.05, "", ha="center", va="center", transform=ax.transAxes, fontsize=16)

def update_bars(low, high, k, found):
    for i, bar in enumerate(bars):
        if low <= i <= high:
            bar.set_color("orange" if i == k else "lightblue")
        else:
            bar.set_color("lightblue")
    if found:
        title.set_text(f"Value {value_to_search} found at index {k}")
    else:
        title.set_text(f"Fibonacci Search - Low: {low}, High: {high}, K: {k}")

def fibonacci_search(arr, x):
    n = len(arr)
    fib_m_2 = 0
    fib_m_1 = 1
    fib_m = fib_m_1 + fib_m_2

    while fib_m < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib_m
        fib_m = fib_m_1 + fib_m_2

    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m_2, n - 1)
        yield offset, i, fib_m
        if arr[i] < x:
            fib_m = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib_m - fib_m_1
            offset = i
        elif arr[i] > x:
            fib_m = fib_m_2
            fib_m_1 -= fib_m_2
            fib_m_2 = fib_m - fib_m_1
        else:
            return i
    if fib_m_1 and arr[offset + 1] == x:
        return offset + 1
    return -1


value_to_search = random.choice(sorted_array)
print(f"Value to search: {value_to_search}")


search_gen = fibonacci_search(sorted_array, value_to_search)


steps = 0
found_index = -1


pause_interval = 0.1  


while True:
    try:
        low, k, _ = next(search_gen)
        if sorted_array[k] == value_to_search:
            found_index = k
            update_bars(low, len(sorted_array) - 1, k, True)
            title.set_text(f"Value {value_to_search} found at index {k} after {steps} steps")
            print(f"Value found at index: {k}")
            print(f"Total steps taken: {steps}")
            print("Time Complexity: O(log n)")
            print("Space Complexity: O(1)")
            plt.draw()  
            plt.pause(2)  
            plt.close()  
            break
        else:
            update_bars(low, len(sorted_array) - 1, k, False)
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
