# Question Link
# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        SumSet = set()
        SumSet.add(0)
        for i in range(len(nums) - 1, -1, -1):
            NewSet = set()
            for s in SumSet:
                if (s + nums[i]) == target:
                    return True
                NewSet.add(s + nums[i])
                NewSet.add(s)
            SumSet = NewSet

        if target in SumSet:
            return True
        else:
            return False
        
"""
I started by checking if the sum of the numbers in the list is odd. If it is, I returned False since an odd sum cannot be split evenly into two equal parts. If the sum is even, I calculated the target value, which is half of the total sum. Next, I created a set called SumSet to keep track of the possible sums that can be formed using the elements of the list. I initialized this set with the value 0. Then, I iterated through the list in reverse order, updating SumSet to include the sums that can be formed by adding the current element or not. For each sum in the current SumSet, I checked if adding the current element equals the target value. If it does, I immediately returned True. Otherwise, I updated the set with the new possible sums. Finally, if the target sum was found in the set after the loop, I returned True; otherwise, I returned False.
"""