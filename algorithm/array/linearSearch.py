"""
Algo :- 
define l_search(arr,value){
    for 0 <= i <= length(arr):
        if arr[i] == value 
        return true
    return false
}
"""

# Defining function

def linearSearch(arr,val):
 for i in range(len(arr)):
    if arr[i] == val:
        return True
 return False



#------------------------------------
# TESTING 

arr1 = [1,2,5,8,6,8,43,2,7,1,9,1]
print(linearSearch(arr1,5))

arr2 = [1,2,5,8,6,8,43,2,7,1,9,1]
print(linearSearch(arr2,55))

arr3 = [1,2,5,8,6,8,43,2,7,1,9,1]
print(linearSearch(arr3,7))

arr4 = [1,2,5,8,6,8,43,2,7,1,9,1]
print(linearSearch(arr4,9))
