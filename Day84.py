# Question Link
# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


"""
I started by initializing three pointers: low, mid, and high. low tracks the boundary for 0s, mid moves through the array to inspect each element, and high tracks the boundary for 2s. Then I created a loop that continues while mid is less than or equal to high, I checked the value at mid. If it was 0, I swapped it with the value at low, incremented both low and mid, and continued. If it was 1, I simply incremented mid to move to the next element. If it was 2, I swapped it with the value at high, and then decremented high, keeping mid in place to check the new value. This approach sorts the array, ensuring all 0s are at the beginning, 1s in the middle, and 2s at the end.
"""