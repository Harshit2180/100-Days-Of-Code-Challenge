# Question Link
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        S1Count, S2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            S1Count[ord(s1[i]) - ord('a')] += 1
            S2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if S1Count[i] == S2Count[i]:
                matches += 1
            else:
                matches += 0

        left = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            S2Count[index] += 1
            if S1Count[index] == S2Count[index]:
                matches += 1
            elif S1Count[index] + 1 == S2Count[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            S2Count[index] -= 1
            if S1Count[index] == S2Count[index]:
                matches += 1
            elif S1Count[index] - 1 == S2Count[index]:
                matches -= 1

            left += 1
        
        return matches == 26

"""
I started by checking if the length of the first string s1 is greater than the second string s2. If it is, I returned False since a 𝘱𝘦𝘳𝘮𝘶𝘵𝘢𝘵𝘪𝘰𝘯 can't exist in that case. Next, I created two frequency arrays, S1Count and S2Count, each with 26 slots, one for each letter in the alphabet. I populated these arrays by counting the frequency of each character in s1 and the first part of s2 that matches the length of s1. I then compared the counts in these arrays to determine how many characters match between s1 and the current window in s2. If all 26 characters match, I returned True. To slide the window over s2, I moved the left pointer one position forward, adjusting the counts in S2Count for the character that exits the window and the one that enters. After each adjustment, I checked if the counts matched and updated the 𝘮𝘢𝘵𝘤𝘩𝘦𝘴 count accordingly. Finally, if I went through the entire s2 without finding a match, I returned False.
"""