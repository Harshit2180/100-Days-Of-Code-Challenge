# Question Link
# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        MinHeap = [(0, k)]
        visit = set()
        t = 0
        while MinHeap:
            w1, n1 = heapq.heappop(MinHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(MinHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
    
"""
I began by creating a dictionary called edges to represent the graph, where each node maps to a list of its neighboring nodes along with the travel time between them. The input times consists of edges defined by two nodes and a weight, so I built this adjacency list using that data. Next, I initialized a min-heap MinHeap starting with the source node k and a time of 0. I also created a set visit to keep track of nodes that have already been processed, and a variable t to store the current maximum time it takes to reach a node. The algorithm proceeds by repeatedly popping the smallest element from the heap, which represents the node with the shortest travel time that hasn't been visited yet. For each node, I updated the time t and checked its neighbors. If the neighbor hasn't been visited, I pushed the neighbor along with its cumulative travel time into the heap. Finally, I returned t if all nodes have been visited, otherwise, I returned -1 indicating that it's impossible to reach all nodes.
"""