# Question Link
# https://leetcode.com/problems/insert-interval/description/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res
    
"""
I started by initializing an empty list res to store the final result. Then, I iterated through the intervals list to handle different cases. If the new interval's end was less than the current interval's start, it meant that the new interval could be inserted before the current one without overlapping. In this case, I added the new interval to the result and returned the remaining intervals as they were. If the new interval's start was greater than the current interval's end, I added the current interval to the result since there was no overlap. However, if there was an overlap between the new interval and the current one, I merged them by adjusting the start and end of the new interval to the minimum and maximum values, respectively. Once all intervals were processed, I added the final merged or unmerged newInterval to the result and returned the updated list.
"""