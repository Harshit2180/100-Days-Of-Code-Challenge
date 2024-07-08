# Question Link
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_set = set(jewels) 
        for i in stones:
            if i in jewels_set:
                count += 1
        return count
    
"""
First, I initialize a variable count to 0 to keep track of the number of jewels found in the stones string. I then convert the jewels string into a set called jewels_set for faster lookup. Next, I loop through each character in the stones list. If the character is in jewels_set, I increment the count by 1. After finishing the loop, I return the value of count, which represents the number of jewels found in the stones list.
"""