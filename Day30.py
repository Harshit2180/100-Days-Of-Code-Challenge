# Question Link
# https://leetcode.com/problems/add-to-array-form-of-integer/description/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = k

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                num[i] = carry % 10
                carry //= 10
                i = i - 1
            else:
                num.insert(0, carry % 10)
                carry //= 10
        return num

"""
I started with the last index of the list num and a variable carry set to k. While either i is greater than or equal to 0 or carry is greater than 0, I performed the following steps: If i is greater than or equal to 0, I added the value at num[i] to carry, updated num[i] to be the last digit of carry (carry % 10), then updated carry to be the remaining part (carry // 10). I decreased i by 1. If i is negative, I inserted the last digit of carry at the beginning of the list num and updated carry as before. Finally, I returned the updated list num.
"""