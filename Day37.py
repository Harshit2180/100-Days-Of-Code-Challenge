# Question Link
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def validparenthesis(OpenCount, CloseCount):
            if OpenCount == CloseCount == n:
                res.append("".join(stack))
                return
            
            if OpenCount < n:
                stack.append("(")
                validparenthesis(OpenCount + 1, CloseCount)
                stack.pop()

            if CloseCount < OpenCount:
                 stack.append(")")
                 validparenthesis(OpenCount, CloseCount + 1)
                 stack.pop()

        validparenthesis(0,0)
        return res
    
"""
 I used a recursive function called validparenthesis to create all valid combinations of parentheses. I started with an empty stack and an empty result list. The function tracks how many open and close parentheses have been used with OpenCount and CloseCount. When both counts reach the target number n, it means we have a valid combination, so I add this combination to the result list. If there are fewer open parentheses than n, I added an open parenthesis to the stack and called the function again to continue building the combination. After checking this path, I removed the open parenthesis. If there are fewer close parentheses than open parentheses, I added a close parenthesis to the stack and called the function again. After checking this path, I removed the close parenthesis. I started the function with both counts set to 0 and returned the list of valid combinations when done.
"""