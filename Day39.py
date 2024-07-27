# Question Link
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        MySet = set()
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in MySet:
                MySet.remove(s[left])
                left += 1
            MySet.add(s[right])
            res = max(res, right - left + 1)

        return res            
    
"""
I used a set called MySet to keep track of unique characters in a substring and initialized res to store the length of the longest substring found. I also set left to 0 to represent the start of the current substring.
I then iterated through the string s with the right pointer. For each character at position right, if it was already in MySet, I removed characters from the set starting from the left pointer until the character at right was no longer in the set. After ensuring all characters between left and right are unique, I added the character at right to MySet.I updated res to be the maximum of its current value or the length of the current substring. Finally, I returned res, which represents the length of the longest substring with unique characters.
"""