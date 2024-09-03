# Question Link
# https://leetcode.com/problems/integer-replacement/description/

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0

        while n != 1:
            if n % 2 == 0:  
                n = n // 2
            else:  
                if n == 3 or (n % 4 == 1):
                    n = n - 1
                else:
                    n = n + 1
            count += 1

        return count


"""
I started by initializing a counter, count, to track the number of steps taken. Then, I created a loop that continues until the given number n is reduced to 1. Inside the loop, I checked whether n is even or odd. If n is even, I divided it by 2. If n is odd, I considered two scenarios: if n is 3 or n modulo 4 equals 1, I subtracted 1 from n, otherwise, I added 1. This approach helps minimize the number of operations needed to reach 1. After each operation, I incremented the count. Once n becomes 1, I exited the loop and returned the count, representing the minimum number of steps needed to reduce n to 1.
"""