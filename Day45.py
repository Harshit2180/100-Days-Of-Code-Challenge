# Question Link
# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return (a & mask) if b > 0 else a
    
"""
I used a variable mask set to 0xffffffff to handle 32-bit integer overflow. Then, I used a loop to perform bitwise operations until there was no carry left to process. In each iteration of the loop, I calculated the carry by performing a bitwise AND between a and b, and then shifted this result left by one position. I updated a by computing the bitwise XOR of a and b, which gives the sum without the carry. I updated b to be the new carry. This loop continued until the carry was zero. After the loop, I used the mask to ensure the result fits within 32-bit limits and returned the final value.
"""