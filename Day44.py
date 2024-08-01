# Question Link
# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
"""
I used two variables, rob1 and rob2, to keep track of the maximum amount of money that can be robbed up to the previous house and the current house, respectively. For each house in the list, I calculated the maximum amount that could be robbed by either taking money from the current house plus the amount from two houses before or just the amount from the previous house. I updated rob1 and rob2 accordingly. Finally, I returned rob2, which contains the maximum money that can be robbed considering all houses.
"""