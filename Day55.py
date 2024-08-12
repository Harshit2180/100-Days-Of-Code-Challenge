# Question Link
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxfreq = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxfreq = max(maxfreq, count[s[right]])

            while (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res

"""
I started by setting up a dictionary count to keep track of how many times each character appears, and variables res for the longest valid substring found, and maxfreq for the highest frequency of any character. I also set left to 0 to mark the beginning of the substring we're looking at. I looped through each character in the string s. For each character, I updated its count in the dictionary and checked if it had the highest frequency so far. I then checked if the current window of characters needed more than k changes to make all characters the same. If so, I moved the left pointer to shrink the window and updated the character counts accordingly. I kept track of the longest valid substring length in res and returned this length at the end.
"""