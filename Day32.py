# Question Link
# https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        MaxHeap = []
        for i in grid:
            MaxHeaps = [-x for x in i]
            heapq.heapify(MaxHeaps)
            MaxHeap.append(MaxHeaps)

        res = 0

        for j in range(len(grid[0])):
            MaxDelete = -float('inf')
            for k in MaxHeap:
                MaxDelete = max(MaxDelete, -heapq.heappop(k))
            res += MaxDelete

        return res 

"""
First, I created an empty list called MaxHeap. For each row in the grid, I converted the elements to their negative values and used heapq.heapify to turn the row into a max-heap. I added each of these max-heaps to the MaxHeap list. Then, I initialized a variable res to 0 to store the result. I iterated through each column index in the grid. For each column, I initialized MaxDelete to negative infinity to keep track of the maximum value in the column. I iterated through each heap in MaxHeap, popped the largest element (which is stored as a negative number, so I negate it to get the original value), and updated MaxDelete to the maximum value. I added MaxDelete to res. Finally, I returned res, which is the sum of the largest elements in each column
"""