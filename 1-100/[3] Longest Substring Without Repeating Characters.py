#
# lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# Question:- 
'''
Longest Substring Without Repeating Characters
Category	Difficulty	Likes	Dislikes
algorithms	Medium (34.82%)	39278	1855

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

# MY_THINKING 
    # algo

"""
    - Make a function which takes a string.
    - Iterate through a for loop for all the characters of that string.
    - Create a dictionary variable where all the characters of the string are going to be stored with their index.
    - For each character, if it is present more than once, remove it from the dictionary.
    - To get the length, initialize a variable and get the maximum of two numbers:
        - One should be zero (because if the input is empty, we might get 1 [because of the second number]).
        - The second number should be the difference between 
          the two pointers plus 1 (the first pointer 'j' tells us about
          the current character position where it stopped the removing, 
          and the second pointer 'i' tells us about the number of characters. 
          As we are taking numbers from 0 [index], we must add 1).
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Initialize variables
        j = 0
        length = 0
        seen = set()

        # Iterate through the string with two pointers
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            length = max(length, i - j + 1)

        return length

#------------------------------------------------------------------------------------------------------------------------

# Testing purpose only 
     # testing the  given inputs in the 
    def test_case(self):
        print(self.lengthOfLongestSubstring("abcabcbb"))        # expect 3
        print(self.lengthOfLongestSubstring("bbbbb"))           # expect 1
        print(self.lengthOfLongestSubstring("pwwkew"))          # expect 3
        print(self.lengthOfLongestSubstring(""))                # expect 0

sol = Solution()
sol.test_case()

