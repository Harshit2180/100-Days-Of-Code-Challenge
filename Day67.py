# Question Link
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
"""
 I started by initializing a result list, res, where each element is set to 1. This list will store the product of all elements in the input list, nums, except for the current element. First, I calculated the prefix product, which is the product of all elements before the current one. I used a variable prefix, initialized to 1, and iterated through nums from left to right, updating the result list with these prefix products. Next, I calculated the postfix product, which is the product of all elements after the current one. I used a similar approach with a variable postfix, iterating through nums in reverse. During this iteration, I multiplied the existing values in the result list with the corresponding postfix products. Finally, I returned the res list, which now contains the product of all elements in nums except for the current element at each index.
"""