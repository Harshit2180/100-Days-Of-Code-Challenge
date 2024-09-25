# Question Link
# https://leetcode.com/problems/asteroid-collision/description/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j = 0
        n = len(asteroids)

        for i in range(n):
            asteroid = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1

            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid
                j += 1
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1
                
        return asteroids[:j]

        
"""
I iterated over the list of asteroids and managed collisions between them. The variable j was used as a pointer to track the position where the current valid asteroid sequence ends. For each asteroid, I checked if there was a possible collision between a positive asteroid moving to the right and a negative asteroid moving to the left. If a collision happened (i.e., a previous asteroid at j-1 was moving right, and the current asteroid was moving left), I compared their sizes. If the previous asteroid was smaller, I removed it by decrementing j. Next, I handled three cases: if there was no collision, if the current asteroid was positive, or if the asteroid at j-1 was negative, in which case I moved the current asteroid to position j. If the two asteroids had equal magnitudes, they both got destroyed, so I reduced j by 1. Finally, I returned the portion of the list that represented the valid sequence of surviving asteroids up to index j.
"""