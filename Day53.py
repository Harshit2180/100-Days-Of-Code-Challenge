# Question link
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left += 1
            else:
                right -= 1
        
        return res
    
"""
I started by initializing res with the first element of the nums list, and set left to 0 and right to the last index of the list. I then created a loop that continued as long as left is less than or equal to right. Inside the loop, if the element at left is less than the element at right, it meant the smallest element was found on the left side, so I updated res to the minimum of res and nums[left] and then broke out of the loop. If the smallest element was not found, I calculated the middle index mid and updated res to the minimum of res and the element at the index mid. If the element at the index mid was greater than or equal to left most element, it meant the smallest element was on the right side, so I moved left to mid + 1. Otherwise, I moved right to mid - 1 to search on the left side. Finally, I returned res, which is the minimum element in the rotated sorted array.
"""