# Question Link
# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for i in s:
            frequency[i] = 1 + frequency.get(i, 0)

        MaxFreq = [(-freq, char) for char, freq in frequency.items()]
        heapq.heapify(MaxFreq)

        res = ""
        while MaxFreq:
            freq, char = heapq.heappop(MaxFreq)
            res += char * (-freq)

        return res

"""
I started by creating a dictionary to count the frequency of each character in the input string. As I iterated through the string, I updated the frequency count for each character. Next, I built a list of tuples, where each tuple contained the negative frequency and the character. This negative frequency was used because the heapq library in Python implements a min-heap, and I needed to simulate a max-heap to prioritize characters with the highest frequency. I then converted this list into a heap using heapify. In the next step, I initialized an empty string res to build the final result. While there were still elements in the heap, I popped the character with the highest frequency and appended it to res, multiplying it by its frequency. Finally, I returned the constructed string, which contains all characters sorted by their frequency in descending order.
"""
