# Question Link
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/descript

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        seen = set()
        duplicate = set()

        for i in nums:
            if i in seen:
                duplicate.add(i)
            else:
                seen.add(i)
        
        for i in duplicate:
            res = res ^ i

        return res

"""
I initialized a variable res to 0 to store the result. I created two sets, seen and duplicate. Iterating through each element i in the nums list, if i was already in the seen set, I added it to the duplicate set, otherwise, I added it to seen. After identifying all duplicates, I iterated through the duplicate set and performed a bitwise XOR on each element i, updating res accordingly. Finally, I returned res.
"""