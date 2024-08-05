# Question Link
# https://leetcode.com/problems/non-overlapping-intervals/descripti

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        count = 0
        PrevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= PrevEnd:
                PrevEnd = end
            else:
                count += 1
                PrevEnd = min(PrevEnd, end)
        
        return count
    
"""
 I began by sorting the list of intervals. Next, I initialized a variable count to keep track of the number of overlapping intervals and set PrevEnd to the endpoint of the first interval. I then looped through the remaining intervals. For each interval, if its starting point was greater than or equal to PrevEnd, it means there was no overlap, so I updated PrevEnd to the current interval's endpoint. If the starting point of the interval was less than PrevEnd, it means there was an overlap. I incremented the count and updated PrevEnd to the minimum of the previous PrevEnd and the current interval's endpoint to account for the overlap. Finally, I returned the total count of overlapping intervals.
"""