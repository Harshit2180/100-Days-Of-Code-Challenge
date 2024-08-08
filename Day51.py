# Question Link
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            freq = [[] for i in range(len(nums) + 1)]
            
            for n in nums:
                count[n] = 1 + count.get(n, 0)
            
            for key, val in count.items():
                freq[val].append(key)
            
            res = []
            for i in range(len(freq)-1, 0, -1):
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
                    
"""
I started by creating a dictionary called count to keep track of how many times each number appears in nums. I also made a list of lists called freq, where each index shows a frequency and stores the numbers with that frequency. First, I counted each number in nums and updated the count dictionary. Then, I used this dictionary to fill the freq list, where each index has a list of numbers that appear that many times. To find the most frequent numbers, I made an empty list called res. I went through the freq list from the highest frequency to the lowest. For each frequency, I added the numbers to res. As soon as res has k numbers, I returned it. If I finished the loop without getting k numbers, res still has the most frequent numbers.
"""