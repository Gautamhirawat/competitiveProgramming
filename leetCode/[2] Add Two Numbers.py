#
#lang=python3
#
# [2] Add Two Numbers
#

#*Add Two Numbers*


# Question:- 
"""

Add Two Numbers
Category	Difficulty	Likes	Dislikes
algorithms	Medium (42.91%)	30649	6089
Tags
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""



# MY_THINKING 
    # algo
"""
    -So we take 2 input as linked list using Optional data structure of typing module , this is not necessary if you are using Leetcode terminal i think they preloaded it . 
    -next we define ListNode - a value (val) and its pointer (next)
    -To solve this question we can be using many approach i used the dividend and reminder approach.
        - It uses the fact that if we divide the sum of both the 'i' integer of the linked list and add a variable carry 
        initially we define it to be 0 , then the total of that if divided by the 10 it gives a remainder and a dividend .
        - the reminder act as digit and Divisor act as carry that can be added in 'i+1' iteration .
        - It ultimately make a reverse of the linked list  normally ,  
"""
# just for testing purpose
from typing import Optional


# SOLUTION
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # just for testing purpose 
    def __str__(self):
        current = self
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get the values of current nodes or 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            
            # Create a new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # This just moves the digit to next if teh space is already occupied
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        return dummy.next



# NOTE This is just for texting purpose the solution ends here only.
#------------------------------------------------------------------------------------------------------------------------

# Testing purpose only 
     # testing the  given inputs in the 
    def run_tests(self):
        # Create linked lists for the inputs
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))

        l3 = ListNode(0)
        l4 = ListNode(0)

        l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

        print(self.addTwoNumbers(l1, l2))   # Expected Output: [7, 0, 8]
        print(self.addTwoNumbers(l3, l4))   # Expected Output: [0]
        print(self.addTwoNumbers(l5, l6))   # Expected Output: [8, 9, 9, 9, 0, 0, 0, 1]


sol = Solution()
sol.run_tests()



