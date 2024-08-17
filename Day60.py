# Question Link
# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
"""
First, I checked if the length of the array is 1. If it is, I returned the money at the first index. Otherwise, I returned the maximum of two scenarios: one where I exclude the first house and one where I exclude the last house. I used two variables, rob1, and rob2, to keep track of the maximum amount of money that can be robbed up to the previous house and the current house. For each house in the list, I calculated the maximum amount that could be robbed by either taking the money from the current house plus the amount from two houses before, or just taking the amount from the previous house. I then updated rob1 and rob2 accordingly. Finally, I returned rob2, which contains the maximum money that can be robbed considering all the houses.
"""