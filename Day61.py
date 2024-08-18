# Question Link
# https://leetcode.com/problems/reverse-integer/description/4

class Solution:
    def reverse(self, x: int) -> int:
        Min = -2147483648
        Max = 2147483647

        num = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if (num < Min//10 or num == Min//10 and digit <= Min % 10):
                return 0

            if (num > Max// 10 or num == Max//10 and digit >= Max % 10):
                return 0

            num = num * 10 + digit

        return num

"""
I started by defining the minimum and maximum values for a 32-bit signed integer. Then, I initialized a variable num to 0, which will store the reversed integer. Next, I entered a loop that continues until the input x becomes 0. In each iteration of the loop, I extracted the last digit of x using the modulus operation and then updated x by removing this last digit. Before updating num, I checked if adding the digit would cause num to exceed the 32-bit signed integer range. If such an overflow or underflow condition is detected, I returned 0 to indicate that the reversed number would be out of bounds. If the digit can be safely added, I updated num by multiplying it by 10 and adding the digit to it. Finally, after the loop completes, I returned num, which now contains the reversed integer.
"""