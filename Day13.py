# Question Link
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        while nums != [0]*n:
            count += 1
            small = min([i for i in nums if i > 0])
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= small
        return count
    
"""
First, I find the length of the nums array and store it in n. I also initialize a variable count to 0 to keep track of the number of operations. I then enter a while loop that continues until all elements in nums are 0. Inside the loop, I increment count by 1. I find the smallest non-zero element in nums and store it in small. Then, I go through each element in nums. If an element is not 0, I subtract small from it. Finally, once the loop completes and all elements in nums are 0, I return the value of count.
"""