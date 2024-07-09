# Question Link
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        MinHeap = []
        for i, row in enumerate(mat):
            SoldiersCount = 0
            for j in range(len(row)):
                if row[j] == 1:
                    SoldiersCount += 1
                else:
                    break
            heapq.heappush(MinHeap, (SoldiersCount, i))
        WeakRow = [heapq.heappop(MinHeap)[1] for w in range(k)]
        return WeakRow
    
"""
First, I created an empty list called MinHeap. Then, I went through each row in the matrix mat. For each row, I counted the number of soldiers (represented by 1s) until I found a 0 or reached the end of the row. I added a pair (number of soldiers, row index) to MinHeap to keep it sorted. After checking all rows, I found the indices of the k weakest rows by taking the smallest elements from MinHeap k times. Finally, I returned these indices as a list WeakRow.
"""