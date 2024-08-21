# Question Link
# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = [intervals[0]]
        for start, end in intervals[1:]:
            PrevEnd = res[-1][1]
            if start <= PrevEnd:
                res[-1][1] = max(end, PrevEnd)
            else:
                res.append([start, end])

        return res

            
"""
I started by sorting the intervals based on their start times. I then initialized the res list with the first interval, as this will serve as the starting point for comparisons. Next, I looped through the remaining intervals. For each interval, I compared its start time with the end time of the last interval in res. If the current interval overlaps with the last one i.e. its start time is less than or equal to the end time, I merged them by updating the end time of the last interval to be the maximum of the two end times. If there is no overlap, I added the current interval to res as a new interval. Finally, I returned the res list, which contains all the merged intervals.
"""