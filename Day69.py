# Question Link
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
                
"""
I started by setting up two pointers, left and right, at the beginning and end of the list, respectively. In each iteration, I calculated the middle index mid and checked if the target matched the value at this index. If it does, I returned the index immediately. If not, I checked whether the left half of the list is sorted by comparing the values at left and mid. If the left half is sorted, I determined if the target is within this range. If it is, I decremented the right pointer to focus on the left half. If not, I incremented the left pointer to focus on the right half. If the left half wasn't sorted, I assumed the right half must be sorted. I then checked if the target lies within the right half. If it does, I incremented the left pointer, otherwise, I decremented the right pointer. I repeated this process until the left pointer surpassed the right, indicating the target wasn't found in the list. In this case, I returned -1 to signify the target isn't present.
"""