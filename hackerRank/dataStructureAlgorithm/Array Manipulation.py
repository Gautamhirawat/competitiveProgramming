def arrayManipulation(n, queries):
    # Initialize array to keep track of differences
    arr = [0] * (n + 1)
    
    # Apply each operation on the difference array
    for query in queries:
        a, b, k = query
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k
    
    # Compute the maximum value using prefix sum
    max_value = 0
    current_value = 0
    for i in range(1, n + 1):
        current_value += arr[i]
        if current_value > max_value:
            max_value = current_value
    
    return max_value





"""
Testing Purpose only
"""
n = 5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

print("Using Difference Array approach",arrayManipulation(n, queries)) 