class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0

        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                count = count - 1
            res = max(res, count)

        return res
    
"""
In this code, I found the maximum depth of the parentheses by creating two variables, res and count, and setting them to zero. I then traversed the string. If the character was an opening parenthesis, I increased the count by 1. If it was a closing parenthesis, I decreased the count by 1. After each change, I updated res to be the maximum of its current value and count. Finally, I returned res.
"""