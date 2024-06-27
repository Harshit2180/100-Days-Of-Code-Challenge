# Question Link
# https://leetcode.com/problems/find-the-town-judge/description/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            if not trust:
                return 1
            else:
                return -1

        trust_count = [0] * (n+1)
        trusted_by = [0] * (n+1)

        for a,b in trust:
            trust_count[b] += 1
            trusted_by[a] += 1

        for i in range(1, n+1):
            if trust_count[i] == n-1 and trusted_by[i] == 0:
                return i
        
        return -1
    
"""
If there is only one person and the trust list is empty, I return 1 because that person is the town judge. If the list isn't empty, I return -1. Then, I create two lists, trust_count and trusted_by, to track how many people trust each person and how many people each person trusts. I update these lists based on the trust pairs. I then check each person to see if they are trusted by n-1 people and trust no one. If I find such a person, I return their number as the town judge. If not, I return -1.
"""