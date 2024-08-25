# Question Link
# https://leetcode.com/problems/maximum-width-ramp/description/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(nums)): 
            if not stack or nums[stack[-1]] > nums[i]: 
                stack.append(i)
                
        for i in range(len(nums)-1, -1, -1): 
            while stack and nums[stack[-1]] <= nums[i]: 
                ans = max(ans, i - stack.pop())

        return ans

"""
I began by initializing ans to store the maximum distance and an empty stack to track indices in the nums list. First, I iterated through nums from left to right, pushing indices onto the stack if the stack is empty or if the current value is less than the value at the top index of the stack. This helps identify potential minimum values. Then, I iterated through nums from right to left, checking if the current value is greater than or equal to the value at the top stack index. If it is, I calculated the distance between the current index and the index from the stack, updating ans with the maximum found, and popped the stack. Finally, I returned ans, which contains the maximum distance meeting the conditions.
"""