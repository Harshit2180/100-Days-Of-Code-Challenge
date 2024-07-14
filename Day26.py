# Question Link
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total

            return dfs(i+1, total ^ nums[i]) + dfs(i+1, total)
        return dfs(0,0)
    
"""
I defined a recursive function called dfs that takes two parameters: i, which represents the current index in the list nums, and total, which represents the current accumulated total. If i is equal to the length of nums, it means we have processed all elements, and I return the current total. Otherwise, I recursively call dfs twice: once by including the current element in the total using XOR (total ^ nums[i]) and once by excluding the current element (total). Finally, I return the sum of these two recursive calls. The initial call to dfs starts at index 0 with a total of 0.
"""