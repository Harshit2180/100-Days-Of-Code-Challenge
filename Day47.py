# Question Link
# https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        MaxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(MaxHeap)

        q = deque()
        time = 0
        while MaxHeap or q:
            time += 1
            if MaxHeap:
                cnt = 1 + heapq.heappop(MaxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(MaxHeap, q.popleft()[0])
                
        return time
    
"""
I first counted the occurrences of each task using a Counter and used these counts to build a max-heap. I also used a queue to track tasks in their cooldown period and initialized the time to 0. I then ran a loop that continued while there were tasks in either the heap or the queue. Each iteration of the loop increased the time by 1. If there were tasks in the heap, I extracted the most frequent task, updated its count, and if it still had remaining instances, added it to the queue with its cooldown period. Additionally, I checked the queue to see if any tasks had completed their cooldown and moved them back to the heap if so. Finally, I returned the total time needed to complete all tasks, including the cooldown periods.
"""