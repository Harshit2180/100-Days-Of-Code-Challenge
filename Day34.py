# Question Link
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_dict = {}

        for i, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = i
        
        result = []
        for num in nums:
            result.append(count_dict[num])

        return result
    
"""
First, I sorted the input list nums into sorted_nums and created an empty dictionary count_dict. I then looped through sorted_nums and recorded the first occurrence index of each number in count_dict. Next, I created an empty list result and filled it with the corresponding indices from count_dict for each number in the original nums list. Finally, I returned the result list.
"""