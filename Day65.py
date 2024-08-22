# Question Link
# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
        
        return res
    
"""
I first checked if the total gas was sufficient to cover the total cost of the journey. If not, I returned -1. Then, I initialized total to track the net gas surplus or deficit as I iterated through the stations, and res to store the potential starting index of a viable circuit. Within the loop, I updated total by adding the difference between the current station's gas and cost. If at any point, the total becomes negative, indicating that starting from the current res index doesn't provide enough gas to continue to the next station, I reset  total to zero and update the res to the index of the next station. Finally, I returned res, which holds the index of the starting station from where a full circuit can be completed successfully.
"""