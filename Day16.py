# Question Link
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if i%3 != 0:
                count += 1

        return count 
    
"""
First, I initialize a count variable to keep track of number of operations. Then I loop through each element and check if it is not divisible by 3. If it isn't, I increase the count variable by 1. After going through all the elements in nums, I return the value of count, which represents the minimum number of operations to make all elements divisible by 3.
"""