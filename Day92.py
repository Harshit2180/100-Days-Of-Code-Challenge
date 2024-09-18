# Question Link
# https://leetcode.com/problems/matchsticks-to-square/description/

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
            TotalSum = sum(matchsticks)
            if TotalSum % 4 != 0:
                return False
            
            target = TotalSum // 4
            matchsticks.sort(reverse=True)  
            
            sides = [0] * 4
            
            def square(index):
                if index == len(matchsticks):
                    return sides[0] == sides[1] == sides[2] == sides[3] == target
                
                for i in range(4):
                    if sides[i] + matchsticks[index] <= target:
                        sides[i] += matchsticks[index]  
                        if square(index + 1):  
                            return True
                        sides[i] -= matchsticks[index]  
                    
                    if sides[i] == 0:
                        break
                
                return False
            
            return square(0)


"""
I started by calculating the total sum of the matchsticks. If this sum wasn’t divisible by 4, I returned False since forming a square would be impossible. Otherwise, I set the target side length by dividing the sum by 4. I sorted the matchsticks in descending order to place the largest ones first. I used a list of four elements to keep track of the lengths of the sides being built. The square function was defined to recursively try placing each matchstick into one of the four sides. For each matchstick, I checked if adding it to a side would keep the side within the target length. If so, I added the matchstick and moved to the next one. If no solution was found, I backtracked by removing the matchstick. If a side remained empty, I stopped further checks as further placements would also fail. Finally, I returned the result of square, starting with the first matchstick.
"""