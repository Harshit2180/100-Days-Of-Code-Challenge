# Question Link
# https://leetcode.com/problems/nth-digit/description/

class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10 

        num = start + (n - 1) // length
        index = (n - 1) % length

        return int(str(num)[index])
    

"""
I began by initializing three variables: length, count, and start to represent the number of digits, the count of numbers with that many digits, and the starting number in that range. I then checked if n exceeds the total digits in the current range. If so, I subtracted this value from n, incremented length to move to the next digit range, multiplied count by 10, and updated start by multiplying it by 10. Once the correct range was found, I identified the number containing the digit. Then, I calculated the position of the digit in the number. Finally, I returned the digit by converting the number to a string and accessing the correct index.
"""