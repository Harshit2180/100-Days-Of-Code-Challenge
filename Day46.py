# Question Link
# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 +1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)
    
"""
I first checked if either number is "0". If so, I returned "0". Then, I created a list res to hold the results of each multiplication. This list is as long as the sum of the lengths of the two numbers. I reversed both input numbers to make the calculation easier from the least significant digit. I then used two nested loops to multiply each digit of num1 with each digit of num2. The result of each multiplication was added to the appropriate position in the res list. I managed carries by adjusting values at the current and next positions in the res list. After completing the multiplications, I reversed the res list to get the correct order. I skipped any leading zeros and converted the remaining numbers to strings. Finally, I joined these strings to form the final result.
"""