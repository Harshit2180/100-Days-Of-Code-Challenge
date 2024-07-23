# Question Link
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            res[tuple(count)].append(word)
        
        return res.values()
    
"""
I used a dictionary called res to group strings from strs by their character counts. For each string in strs, I created a list count to keep track of how many times each letter appears. I then converted this list into a tuple and used it as a key in the res dictionary to group all strings with the same character counts. Finally, I returned the values of the dictionary which is the required list of anagrams grouped together.
"""