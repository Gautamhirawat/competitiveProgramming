def selectionsort(a):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
                if a[min_idx] > a[j]:
                    min_idx = j
        
        a[i], a[min_idx] = a[min_idx], a[i]  
    print("Selection sort")
    for i in range(len(a)):
        print(a[i] , end = " ") 

B = [64, 25, 12, 22, 11]
selectionsort(B)



""" 
# Better version by gpt.

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        if min_idx != i:  # Swap only if needed
            a[i], a[min_idx] = a[min_idx], a[i]

def print_array(a):
    print("Selection sort")
    for element in a:
        print(element, end=" ")
    print()  # for newline

B = [64, 25, 12, 22, 11]
selection_sort(B)
print_array(B)


# Reduces unnecessary swaps.
# Separates the sorting logic from the printing logic for better readability and maintainability.
# Ensures the output is more structured by adding a newline after printing the array
 """