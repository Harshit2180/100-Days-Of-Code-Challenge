# Question Link
# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        OneCount = s.count("1")
        ZeroCount = len(s) - OneCount

        res = "1"*(OneCount - 1) + "0"*(ZeroCount) + "1"
        return res

"""
First, I count how many '1's are in the string and call this OneCount. Then, I find the number of '0's in the string by subtracting OneCount from the total length of the string. Next, I create a string res that has OneCount - 1 '1's at the beginning, followed by ZeroCount '0's, and then one more '1' at the end. This arrangement ensures that the number is maximized and is odd. Finally, I return the res string.
"""