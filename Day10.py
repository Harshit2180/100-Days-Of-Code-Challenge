# Question Link
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            if num%2 == 0:
                num = num/2
            else:
                num -= 1
            step +=1
        return step

"""
I begin with a variable step initialized to zero. Using a while loop that continues as long as num is not zero, I check if num is even. If it is, I divide num by two. If num is odd, I subtract one from it. After each operation, I increment the step variable by one. When num finally becomes zero, I return the value stored in the step variable.
"""
