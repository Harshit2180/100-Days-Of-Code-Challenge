# Question Link
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0
        right = len(nums) - 1
        avg = float('inf')

        while left < right:
            a = nums[left]
            b = nums[right]
            avg = min(avg, (a+b)/2)
            left += 1
            right -= 1
            
        return avg
    
"""
 First, I sorted the list nums and set two pointers, left at the start and right at the end. I initialized a variable avg to infinity to track the smallest average. Then, I created a while loop that will execute until left is less than right. Inside the loop, I assign the values at the left and right pointers to a and b, respectively. I calculate the average of a and b, and update avg if this new average is smaller than the current value of avg. I then increment left by 1 and decrement right by 1 to move the pointers towards the center. After the loop finishes, I return the value of avg, which is the smallest average of pairs from the list.
"""