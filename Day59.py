# Question Link
# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
    
"""
I started by determining the number of rows and columns in the grid, and I initialized a queue (q) using deque. I also set up variables time to track the minutes passed and fresh to count the number of fresh oranges. Next, I looped through the grid to count how many fresh oranges were present and to identify the positions of rotten oranges, which I added to the queue. I then defined the possible directions for the spread of rot as right, left, down, and up using a list of coordinates. While there are still rotten oranges in the queue and fresh oranges to infect, I looped through the queue, processing each rotten orange. For each rotten orange, I checked its neighboring cells in all four directions. If a neighboring cell contained a fresh orange, I marked it as rotten, added it to the queue, and decreased the fresh orange count by one. After processing all the rotten oranges in the queue, I incremented the time by one minute. Finally, I returned the total time if all fresh oranges were rotted, or -1 if there were still fresh oranges left that couldn't be reached.
"""