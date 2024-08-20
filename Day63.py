# Question Link
# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        MinHeap = []

        for x, y in points:
            distance = x**2 + y**2
            MinHeap.append([distance, x, y])

        heapq.heapify(MinHeap)
        res = []

        while k > 0:
            distance, x, y = heapq.heappop(MinHeap)
            res.append([x, y])
            k -= 1
        
        return res
    
"""
I started by creating a list called MinHeap to store the points with their squared distances from the origin. For each point, I calculated the squared distance and added this distance along with the point's coordinates to MinHeap. Next, I converted this list into a min-heap, which organizes the points based on their distances in ascending order. I then initialized an empty list res to store the k closest points. I then created a loop that runs k times and removed the point with the 𝘴𝘮𝘢𝘭𝘭𝘦𝘴𝘵 distance from the heap and added this point to res. Finally, I returned the list res, which contains the k points closest to the origin.
"""