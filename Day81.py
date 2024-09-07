# Question Link
# https://leetcode.com/problems/hand-of-straights/description/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        MinHeap = list(count.keys())
        heapq.heapify(MinHeap)

        while MinHeap:
            first = MinHeap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != MinHeap[0]:
                        return False
                    heapq.heappop(MinHeap)
        
        return True

        
"""
I began by checking if the length of hand is divisible by groupSize. If not, it's impossible to form groups of the required size, so I returned False. Next, I created a count dictionary to track the frequency of each card in hand. I then constructed a min-heap MinHeap from the dictionary keys to ensure I always start grouping from the smallest card. In the loop, I used the smallest card in the heap first to form a group of consecutive cards. For each card from first to first + groupSize - 1, I checked if the card exists in the count dictionary. If it didn’t, the grouping wasn't possible, so I returned False. For valid cards, I reduced their count, and if the count reached zero, I removed the card from the heap. Finally, if all groups were formed successfully, I returned True.
"""