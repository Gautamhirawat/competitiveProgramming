def rotateLeft(d, arr):
    temp = [] ## temporary array
    n=len(arr)
    for i in range(d, n):
        temp.append(arr[i])
    i = 0
    for i in range(0, d):
        temp.append(arr[i])
    arr=temp.copy()
    return arr

    
def rotateLeft2(d, arr):
    n=len(arr) #Slicing 
    arr[:]=arr[d:n]+arr[0:d]
    return arr
    

# theoretically, both approaches have the same time and space complexity.

"""
Testing Purpose only
"""

d1 , arr1 = 2 , [1,2,3,4,5] 
d2 , arr2 = 2 , [1,2,3,4,5] 

d3 , arr3 = 3 , [1,2,3,4,5] 
d4 , arr4 = 3 , [1,2,3,4,5] 

print("Using temporary array approach:", rotateLeft(d1, arr1))
print("Using Slicing approach:", rotateLeft2(d2, arr2))
print("")
print("")
print("Using temporary array approach:", rotateLeft(d3, arr3))
print("Using Slicing approach:", rotateLeft2(d4, arr4))
