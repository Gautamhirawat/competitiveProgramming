# lang=python3
#
# [1] Two Sum

#*Two Sum*


# Question:- 
"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""



# MY_THINKING 
    # algo
"""
    --- make a function which return the answer in list
    --- we need 2 inputs , so make first input to be list and another to be int type .
    --- make a empty dict{} it will be storing the index of - list
    --- now we run for loop in our list and see if the other no to make teh target is present in the list 
    --- if it is then we just return the dict stored index of the other no , and the current no in order . 
"""
# SOLUTION

class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:    # 2 input parameter and 1 output parameter 
        abc = {}                                                    # blank dict 
        for i in range(len(nums)):                                  # iterating through the list 
            y = target - nums[i]                                    # Used to find the other no and stored as y
            if y in abc: 
                return [abc[y],i]                                   # You can change the order with [abc[y],i]
            abc[nums[i]] = i                                        # saving the current no in list with its index 
        return []



# NOTE This is just for texting purpose the solution ends here only.
#------------------------------------------------------------------------------------------------------------------------

# Testing purpose only 
     # testing the  given inputs in the 
    def run_tests(self):
        print(self.twoSum([2,7,11,15], 9))   # Expected Output: [0, 1]
        print(self.twoSum([3,2,4], 6))       # Expected Output: [1, 2]
        print(self.twoSum([3,3], 6))         # Expected Output: [0, 1]

sol = Solution()
sol.run_tests()

        

