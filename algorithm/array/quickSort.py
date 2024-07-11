def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_optimized(a):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(a, 0, len(a) - 1)

def print_array(a):
    print("Quick sort")
    for element in a:
        print(element, end=" ")
    print()  # for newline

# Example usage
B = [64, 34, 25, 12, 22, 11, 90]
B = quick_sort(B)
print_array(B)

B = [64, 34, 25, 12, 22, 11, 90]
quick_sort_optimized(B)
print_array(B)

"""
Average Time Complexity: O(n log n)
Worst Case Time Complexity: O(n^2)
Space Complexity: O(log n) for the recursive stack
Use Case: General-purpose sorting with good average-case performance.
"""
