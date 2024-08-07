# Question Link
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            TempPrices = prices.copy()
            for source, dest, cost in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + cost < TempPrices[dest]:
                    TempPrices[dest] = prices[source] + cost
            
            prices = TempPrices
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]
        
"""
I started by creating a list called prices to store the minimum cost to reach each city. I set the cost to reach the source city to 0, and all other cities to infinity. Next, I ran a loop up to k + 1 times. I made a copy of the prices list called TempPrices to temporarily store updated costs. Inside this loop, I checked each flight and updated the cost to reach the destination city if using this flight provided a cheaper option. Specifically, if the current known cost to reach the source city plus the flight cost was less than the known cost to reach the destination city, I updated TempPrices for the destination city. After processing all flights, I updated prices to be the new costs in TempPrices. Finally, I checked if the cost to reach the destination city is still infinite. If it is, it means the destination is unreachable with the given flights and I returned -1. Otherwise, I returned the minimum cost to reach the destination city.
"""