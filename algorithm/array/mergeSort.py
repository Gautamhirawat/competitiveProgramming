def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left_half = a[:mid]
        right_half = a[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_optimized(a):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left_half = merge_sort_optimized(a[:mid])
    right_half = merge_sort_optimized(a[mid:])

    return merge(left_half, right_half)

def print_array(a):
    print("Merge sort")
    for element in a:
        print(element, end=" ")
    print()  # for newline

# Example usage
B = [64, 34, 25, 12, 22, 11, 90]
merge_sort(B)
print_array(B)

B = [64, 34, 25, 12, 22, 11, 90]
B = merge_sort_optimized(B)
print_array(B)

"""
Time Complexity: O(nlog(n))
Space Complexity: O(n)
Use Case: Stable sorting, consistent performance, works well with large datasets and linked lists.
"""
