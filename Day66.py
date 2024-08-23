# Question Link
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj = {i:[] for i in range(n)} #i:[] list of [cost, node]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        MinH = [[0,0]]  # [cost, point]
        while len(visit) < n:
            cost, i = heapq.heappop(MinH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for NeiCost, Nei in adj[i]:
                if Nei not in visit:
                    heapq.heappush(MinH, [NeiCost, Nei])
        
        return res

"""
I started by determining the number of points and creating an adjacency list adj to store the distances between all pairs of points. For each pair of points, I calculated the Manhattan distance and added it to the adjacency list for both points. I then initialized res to keep track of the total minimum cost, a set visit to track the points that have been visited, and a min-heap MinH to explore the points based on the minimum cost. Using a while loop, I continued to pop the point with the smallest cost from MinH, ensuring that it hadn't been visited before adding its cost to res and marking it as visited. For each unvisited neighboring point, I pushed its distance and index onto MinH. The loop continued until all points were visited, ensuring that the minimum cost to connect all points was calculated. Finally, I returned res, which contains the total minimum cost to connect all the points.
"""
