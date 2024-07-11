# Question Link
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def FirstPosIndex(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
    
        def LastNegIndex(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        FirstPosIdx =  FirstPosIndex(nums)
        LastNegIdx = LastNegIndex(nums)
        
        PosCount = len(nums) - FirstPosIdx
        NegCount = LastNegIdx + 1
        
        return max(PosCount, NegCount)


"""
I defined two functions, FirstPosIndex and LastNegIndex, to find the first positive and last negative numbers in the sorted list nums using binary search. FirstPosIndex moves pointers to locate the index of the first positive number, while LastNegIndex does the same for the last negative number. After finding these indices, I calculated the counts of positive and negative numbers as PosCount and NegCount. Finally, I returned the larger of these two counts.
"""