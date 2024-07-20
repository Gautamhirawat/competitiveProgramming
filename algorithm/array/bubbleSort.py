def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubble_sort_optimized(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break


def print_array(a):
    print("Bubble sort")
    for element in a:
        print(element, end=" ")
    print()  # for newline


# Example usage
B = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(B)
print_array(B)

B = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_optimized(B)
print_array(B)
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
Use Case: Simple implementation for small datasets. The optimized version breaks early if the array is already sorted.
"""
