# Question Link
# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for ind, val in enumerate(nums):
            if ind > 0  and val == nums[ind-1]:
                continue
            
            left = ind + 1
            right = len(nums) - 1
            while left < right:
                ThreeSum = val + nums[left] + nums[right]
                if ThreeSum > 0:
                    right -= 1
                elif ThreeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
        return res
    
"""
First, I sorted the list 𝘯𝘶𝘮𝘴 and initialized an empty list res to store the results. Then, I looped through each element in 𝘯𝘶𝘮𝘴. For each element, I checked if it was a duplicate of the previous one, if it was, I skipped it to avoid duplicate results. For each unique element, I used two pointers to find pairs that, along with the current element, sum to zero. I set the left pointer to the next element and the right pointer to the end of the list. If the sum of the three numbers was greater than zero, I decremented the right pointer by 1. If it was less than zero, I incremented the left pointer by 1. If the sum was zero, I added the triplet to the results list and incremented the left by 1, skipping over any duplicate values to avoid repeating results. Finally, I returned the list of triplets.
"""