# Question Link
# https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        MySet = set(nums1)
        res = []

        for i in nums2:
            if i in MySet:
                res.append(i)
                MySet.remove(i)

        return res
    
"""
I created a set from the array nums1 and an empty array called res. Then, I traversed through each number in the array nums2. If the number was in the set, I added it to the res array and removed it from the set to avoid duplicates in res. After traversing through all the numbers in the nums2 array, I returned the res array.
"""