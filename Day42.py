# Question Link
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
    
"""
I started with an empty list res to store all the subsets of the list nums, and an empty list subset to build each subset. I defined a recursive function dfs that takes an index i as a parameter. The function explores all possible subsets starting from index I. Inside dfs, if the index i is less than or equal to the length of nums, I added a copy of subset to res because I've found a complete subset. Otherwise, I first included nums[i] in subset and called dfs recursively to explore subsets that include this element. Then, I removed nums[i] from subset to backtrack and called dfs again to explore subsets that do not include this element. I started the recursion with index 0 and finally returned the list res, which contains all possible subsets of nums.
"""