# Question Link
# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        NumSet = set(nums)
        LongestStreak = 0

        for i in NumSet:
            if i - 1 not in NumSet:
                current = i
                CurrentStreak = 1

                while current + 1 in NumSet:
                    current += 1
                    CurrentStreak += 1

                LongestStreak = max(LongestStreak, CurrentStreak)

        return LongestStreak

        
"""
I started by checking if the input list nums is empty. If it is, I returned 0, as there would be no sequence. Then, I converted nums into a set NumSet to allow for efficient lookups. I initialized LongestStreak to track the maximum consecutive sequence length. For each number in NumSet, I checked if it is the start of a sequence by ensuring that the previous number is not in the set. If it is the start, I initiated a CurrentStreak and iterated through the consecutive numbers by checking if current + 1 exists in the set. Each time a consecutive number was found, I incremented the CurrentStreak. Finally, I updated LongestStreak with the maximum value between the current streak and the previously tracked longest streak. After processing all the numbers, I returned LongestStreak, which represents the length of the longest consecutive sequence.
"""