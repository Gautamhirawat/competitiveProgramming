def miniMaxSum(arr):
   arr.sort()
   min= sum(arr[:-1])
   max=sum(arr[1:])
   print(min,max) 



# Testing 

miniMaxSum([1, 2, 3, 4, 5])
miniMaxSum([7, 69, 2, 221, 8974])
miniMaxSum([5, 5, 5, 5, 5, 5])
