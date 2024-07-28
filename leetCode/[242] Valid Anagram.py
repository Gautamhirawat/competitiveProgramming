class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)

        if len(count1) != len(count2):
            return False

        for k in count1:
            if count1[k] != count2[k]:
                return False

        return True



#another sol

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
