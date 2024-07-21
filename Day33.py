# Question Link
# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        NumTickets = tickets[k]
        Time = 0
        pointer = 0

        while NumTickets != 0:
            if tickets[pointer] > 0:
                tickets[pointer] -= 1
                Time += 1
                if pointer == k:
                    NumTickets -= 1
            pointer = (pointer + 1) % len(tickets)

        return Time
    
"""
 I started by getting the number of tickets at position k and set time to 0 and pointer to 0 to keep track of the current index in the tickets list. Then, I used a while loop to process tickets until NumTickets reached 0. Inside the loop, I checked if the current ticket count at the pointer index is greater than 0. If so, I decremented the ticket count at this index, increased the Time by 1, and if the pointer index is equal to k, I decremented NumTickets by 1. I then moved the pointer to the next index in a circular manner by using the modulo operation with the length of tickets. Finally, I returned the total Time taken to process all tickets at position k.
"""