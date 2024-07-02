# Question Link
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = ""

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            else:
                res += first[i]
        return res
    
"""
First, I sorted the list of strings strs. I initialized an empty string res to store the result. Then, I called the first and the last strings of this sorted list first and last, respectively. I looped through each character position up to the length of the shorter string between first and last. If the characters at the current position in first and last are different, I return res. If the characters are the same, I add the character from first to res. After the loop, I return res, which contains the common prefix.
"""