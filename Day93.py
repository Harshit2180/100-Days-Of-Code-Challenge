# Question Link
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
                        

"""
I began by checking if the grid was empty, returning 0 if it was. Then, I calculated the number of rows and columns in the grid and created a set to track visited cells. I also initialized a variable islands to count the number of distinct islands. I defined a helper function bfs to perform a breadth-first search (BFS) from a starting cell. This function took the row and column indices of a cell, added them to the visit set, and used a queue to explore all its connected land cells. For each cell, I checked its four neighboring cells, up, down, left, and right. If a neighbor was a valid unvisited land cell i.e., marked as "1" in the grid, I added it to the queue and marked it as visited. After defining bfs, I iterated through every cell in the grid. If I found an unvisited land cell, I called bfs to explore the entire island and incremented the islands counter. Finally, I returned the total number of islands counted.
"""