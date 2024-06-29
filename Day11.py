# Question Link
# https://leetcode.com/problems/fibonacci-number/description/

class Solution:
     def fib(self, n: int) -> int:
        if n <= 1:
            return n

        Fibo = [0] * (n+1)

        Fibo[0] = 0
        Fibo[1] = 1

        for i in range(2,n+1):
            Fibo[i] = Fibo[i-1] + Fibo[i-2]

        return Fibo[n]
     
"""
First, I check the value of n. If it is less than or equal to one, I return n. Otherwise, I create a list called Fibo with n+1 elements and set the first two elements to zero and one, respectively, because these are the first two numbers in the Fibonacci sequence. Then, I use a for loop to fill in the rest of the list. For each index from 2 to n, I set Fibo[i] to the sum of the two previous elements, Fibo[i-1] and Fibo[i-2]. Finally, I return the nth element of the Fibo list.
"""