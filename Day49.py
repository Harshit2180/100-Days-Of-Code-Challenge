# Question Link
# https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        JumpCount = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            
            left = right + 1
            right = farthest
            JumpCount += 1
        
        return JumpCount
    
"""
I started by initializing variables: JumpCount to count the number of jumps, and left and right to track the current range of indices that can be reached with the current number of jumps. In a loop that continues until right reaches or exceeds the last index of the list, I found the farthest index that can be reached from the current range [left, right]. I did this by iterating through each index in this range and calculating how far I could jump from there. After determining the farthest reachable index, I updated left to be the next index after right and set right to the farthest index found. I then incremented JumpCount by 1 to count the jump. Finally, I returned the total number of jumps needed to reach the end of the list.
"""