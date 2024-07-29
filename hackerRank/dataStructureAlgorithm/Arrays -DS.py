def reverseArray1(a): 
    left = 0 
    right = len(a) - 1
    
    while(left < right): # Two Pointer Method # #O(n) TIME  and O(1) SPACE
        a[left] , a[right] = a[right], a[left]
        left += 1
        right -= 1
    
    return a


def reverseArray2(b):
    b.reverse() # reverse() or Reversed() #O(n) TIME  and O(1) SPACE
    return b

def reverseArray3(c):

  return c[::-1] # Slicing  # O(n) and O(n)


"""
Testing Purpose only
"""

arr1 = [1,4,3,2]
arr2 = [1,4,3,2]
arr3= [1,4,3,2]

print("Using two-pointer approach:", reverseArray1(arr1))
print("Using Inbuilt reverse approach:", reverseArray2(arr2))
print("Using slicing approach:", reverseArray3(arr3))
