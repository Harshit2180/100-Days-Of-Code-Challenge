# Question Link
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
    
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
        
        return heap[0]


"""
I started by initializing an empty heap to keep track of the top k largest numbers in the list. I then iterated through the nums array. For the first k numbers, I added each one to the heap. Once the heap contained k elements, I compared each remaining number in nums with the smallest element in the heap, which is always at the root. If the current number was larger than the smallest element, I replaced the root. Finally, after processing all numbers, the smallest element in the heap represents the kth largest number, which I returned as the result.
"""