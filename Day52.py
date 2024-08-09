# Question Link
# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[] for i in range(len(position))]

        for i in range(len(position)):
            pair[i].append(position[i])
            
        for k in range(len(speed)):
            pair[k].append(speed[k])

        stack = []
        for pos, sp in sorted(pair)[::-1]:
            stack.append((target - pos)/sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

"""
I started by creating a list of lists called pair, where each inner list will hold a position and its corresponding speed. Next, I prepared an empty list called stack to help track the times needed for cars to reach the target. I then processed each car by sorting the pair list in descending order based on positions and speeds. For each car, I calculated the time it would take to reach the target and added this time to the stack. While adding times to the stack, I checked if the last time was less than or equal to the second-to-last time in the stack. If so, it meant that the current car would reach the target before or at the same time as the previous car, so I removed the last time from the stack to avoid unnecessary entries. Finally, I returned the number of entries left in the stack, which represents the number of car fleets that will reach the target together.
"""