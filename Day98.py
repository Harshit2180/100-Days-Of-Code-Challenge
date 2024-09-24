# Question Link
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        MaxLen = 1
        MaxStr = s[0]
        for i in range(len(s)- 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > MaxLen and s[i: j + 1] == s[i: j + 1][::-1]:
                    MaxLen = j - i + 1
                    MaxStr = s[i: j + 1]

        return MaxStr

        
"""
I first checked if the string s has a length of 1 or less, and if so, I returned the string itself since it's already a palindrome. Otherwise, I initialized two variables: MaxLen to store the length of the longest palindromic substring found, starting at 1, and MaxStr to store the longest palindrome found so far, which initially is the first character. Then, I used a nested loop to iterate through all possible substrings in s. For each pair of indices i and j, I checked if the substring s[i: j + 1] was a palindrome and if its length was greater than the current MaxLen. If both conditions were met, I updated MaxLen and set MaxStr to the new longest palindrome. After checking all possible substrings, I returned MaxStr, which contained the longest palindromic substring.
"""