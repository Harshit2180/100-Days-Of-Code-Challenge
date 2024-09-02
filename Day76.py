# Question Link
# https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        
        return area

        
"""
I started by determining the number of rows and columns in the grid and initializing a set called visit to keep track of the cells that have been visited. Then, I defined a depth-first search dfs function that takes the current row and column as arguments. Inside the dfs function, I checked if the current position is out of bounds, contains water, or has already been visited. If any of these conditions are met, I returned 0, indicating that this path does not contribute to the area. If the current cell is valid, I marked it as visited and recursively called the dfs function for its neighboring cells up, down, left, and right. The function returned the total area by adding 1 for the current cell to the areas returned by the recursive calls. To find the maximum area of an island, I iterated through each cell in the grid. For each cell, I called the dfs function and updated the maximum area found. Finally, I returned the maximum area.
"""