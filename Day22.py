# Question Link
# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()  
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] <= nums[i]:
                    res = max(res, nums[i] ^ nums[j])
                else:
                    break  

        return res            

"""
First, I sorted the list nums. I set a variable res to 0 to store the highest result. Then, I got the length of nums and saved it in n. I used two loops to go through the list: the first loop goes through each element, and the second loop goes through each element after the first one. If the difference between the second and first element is less than or equal to the first element, I update res to be the highest of its current value or the XOR of the two elements. If the difference is greater, I stop the inner loop and move to the next element in the outer loop. Finally, I return res, which is the highest XOR value I found.
"""
