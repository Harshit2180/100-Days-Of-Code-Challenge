# Question Link
# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for i in t:
            count[i] = count.get(i,0) + 1

        for j in s:
            count[j] -= 1
            if count[j] == 0:
                del count[j]
        
        return list(count.keys())[0]

"""
I created an empty dictionary called count to keep track of characters in the string t. For each character in t, I added it to the dictionary and increased its count. Then, I went through each character in the string s and decreased its count in the dictionary. If any character's count reached zero, I removed it from the dictionary. In the end, I returned the only character left in the dictionary, which is the extra character in t.
"""