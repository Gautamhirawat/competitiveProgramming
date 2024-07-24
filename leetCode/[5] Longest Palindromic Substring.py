
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join(f"^{s}$")
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n-1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R, adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        start = (center_index - max_len) // 2  # start index of the longest palindromic substring
        return s[start: start + max_len]



"""
        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left, right):
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Update the start and end to the longest palindromic substring found
            if (right - left - 1) > (end - start):
                start = left + 1
                end = right - 1

        for i in range(len(s)):
            # Odd length palindromes (single character center)
            expand_around_center(i, i)
            # Even length palindromes (two character center)
            if i + 1 < len(s):
                expand_around_center(i, i + 1)

        return s[start:end+1]
"""
