# Question Link
# https://leetcode.com/problems/find-center-of-star-graph/description/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        node_count = [0] * (n+1)
        for a,b in edges:
            node_count[a] += 1
            node_count[b] += 1
            
        for i in range(1, n+1):
            if node_count[i] == n - 1:
                return i       

"""
First, I calculated the number of nodes by adding 1 to the length of the edges list. Then, I created a list called node_count of length n + 1 to keep track of the count of edges connected to each node. I looped through each pair of nodes in edges and incremented the count for both nodes in the node_count list. After processing all edges, I looped through the node_count list from 1 to n. If a node's count is equal to n - 1, it means this node is connected to all other nodes, and I return this node as the center of the star graph.
"""