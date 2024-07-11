def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def insertion_sort_optimized(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def print_array(a):
    print("Insertion sort")
    for element in a:
        print(element, end=" ")
    print()  # for newline

# Example usage
B = [64, 25, 12, 22, 11]
insertion_sort(B)
print_array(B)

B = [64, 25, 12, 22, 11]
insertion_sort_optimized(B)
print_array(B)

"""
Time Complexity: O(n^2)
Best Case Time Complexity: O(n)
Space Complexity: O(1)
Use Case: Efficient for small or nearly sorted datasets.
"""
