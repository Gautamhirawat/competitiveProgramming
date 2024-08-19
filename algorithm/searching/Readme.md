# Search Algorithms Visualization

This project demonstrates various search algorithms by visualizing their execution. It includes scripts to run different search algorithms, record their execution, and convert the recordings into GIF animations for demonstration purposes.

## Project Structure


- `linear_search.py`: Script to perform Linear Search.
- `binary_search.py`: Script to perform Binary Search.
- `jump_search.py`: Script to perform Jump Search.
- `exponential_search.py`: Script to perform Exponential Search.
- `hashing_search.py`: Script to perform Hashing Search.
- `best_first_search.py`: Script to perform Best-First Search.
- `dfs_search.py`: Script to perform Depth-First Search (DFS).
- `bfs_search.py`: Script to perform Breadth-First Search (BFS).
- `fibonacci_search.py`: Script to perform Fibonacci Search.
- `ternary_search.py`: Script to perform Ternary Search.
- `interpolation_search.py`: Script to perform Interpolation Search.
- `record_and_convert.py`: Script to record each algorithm execution and convert it to GIF.

## Requirements

- python 3
- `pandas` (for data handling)
- `matplotlib` (for displaying summary tables)

You can install the required Python packages using pip:

```bash
pip install pandas matplotlib
```

## How to Use

Run All Scripts Seperately or you can run main file

```bash
python3 main.py
```

Now you can run any of the above files or there is another option that can be used to run all files one after another.

## Conclusion 


1.  `Linear Search`: Sequentially checks each element until it finds the target or exhausts the list.

```
    def linear_search(arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1
    
```


2.  `Binary Search`: Efficiently finds the target in a sorted list by repeatedly dividing the search interval in half.


```
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
```


3.  `Jump Search`: Jumps ahead by a fixed number of steps and then performs a linear search within the block.
```
    import math

    def jump_search(arr, target):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n)-1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev] == target:
            return prev
        return -1

```
4.  `Exponential Search`: Exponentially increases the search range and then uses binary search within the identified range.


```
    def exponential_search(arr, target):
        if arr[0] == target:
            return 0
        index = 1
        while index < len(arr) and arr[index] <= target:
            index *= 2
        left, right = index // 2, min(index, len(arr) - 1)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

```
5.  `Fibonacci Search`: Uses Fibonacci numbers to reduce the search range in a sorted list.

```

    def fibonacci_search(arr, target):
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
            if arr[i] < target:
                fib_m = fib_m_1
                fib_m_1 = fib_m_2
                fib_m_2 = fib_m - fib_m_1
                offset = i
            elif arr[i] > target:
                fib_m = fib_m_2
                fib_m_1 -= fib_m_1
                fib_m_2 = fib_m - fib_m_1
            else:
                return i
        if fib_m_1 and arr[offset + 1] == target:
            return offset + 1
        return -1

```
6.  `Ternary Search`: Divides the search interval into three parts and recursively searches in the relevant segment.


```
    def ternary_search(arr, target):
        def ternary_search_helper(arr, l, r, target):
            if r >= l:
                one_third = l + (r - l) // 3
                two_third = r - (r - l) // 3

                if arr[one_third] == target:
                    return one_third
                if arr[two_third] == target:
                    return two_third

                if target < arr[one_third]:
                    return ternary_search_helper(arr, l, one_third - 1, target)
                elif target > arr[two_third]:
                    return ternary_search_helper(arr, two_third + 1, r, target)
                else:
                    return ternary_search_helper(arr, one_third + 1, two_third - 1, target)
            return -1
        
        return ternary_search_helper(arr, 0, len(arr) - 1, target)

```
7.  `Interpolation Search`: Uses the value of the target to estimate its position in a sorted list and then searches around that position.

```

    def interpolation_search(arr, target):
        lo, hi = 0, len(arr) - 1
        while lo <= hi and target >= arr[lo] and target <= arr[hi]:
            if lo == hi:
                if arr[lo] == target:
                    return lo
                return -1
            pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (target - arr[lo])))
            if arr[pos] == target:
                return pos
            if arr[pos] < target:
                lo = pos + 1
            else:
                hi = pos - 1
        return -1

```

8.  `Hashing Search`: Uses a hash table to provide constant time complexity for search operations.

```
    class HashTable:
        def __init__(self):
            self.table = {}

        def insert(self, key, value):
            self.table[key] = value

        def search(self, key):
            if key in self.table:
                return self.table[key]
            return None

    def hashing_search(arr, target):
        # Create a hash table and insert elements
        hash_table = HashTable()
        for index, value in enumerate(arr):
            hash_table.insert(value, index)
        
        # Search for the target value
        result = hash_table.search(target)
        if result is not None:
            return result
        return -1
        
```
