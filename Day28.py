# Question Link
# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        Tribo = [0] * (n+1)

        Tribo[0] = 0
        Tribo[1] = 1
        Tribo[2] = 1

        for i in range(3, n+1):
            Tribo[i] = Tribo[i-1] + Tribo[i-2] + Tribo[i-3]
        
        return Tribo[n]

"""
First, I checked the value of n. If it is zero, then I returned zero. If it is one or two, I returned one. Otherwise, I created a list called Tribo with n+1 elements and set the first three elements to 0, 1, and 1, respectively, because these are the first three numbers in the Tribonacci sequence. Then, I used a for loop to fill in the rest of the list. For each index from 3 to n, I set Tribo[i] to the sum of the three previous elements, Tribo[i-1], Tribo[i-2], and Tribo[i-3]. Finally, I returned the nth element of the Tribo list.
"""