# Question Link
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1 , str2):
            len_str1 = len(str1)
            len_str2 = len(str2)

            if len_str1 > len_str2:
                return False

            for i in range(len_str1):
                if str1[i] != str2[i]:
                    return False

            for i in range(len_str1):
                if str1[i] != str2[len_str2 - len_str1 + i]:
                    return False

            return True

        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count

""""
First, I defined a function isPrefixAndSuffix that checks if str1 is both a prefix and a suffix of str2. I calculated the lengths of both strings. If the length of str1 is greater than str2, I returned False. Otherwise, I checked if each character in str1 matches the corresponding character at the beginning and end of str2. If any character doesn't match, I returned False. If all characters match, I returned True. Then, I initialized a variable count to 0 to keep track of the number of times a word is both a prefix and a suffix of another word. I iterated through each pair of words in the list words. If isPrefixAndSuffix returned True for a pair of words, I incremented count by 1. Finally, I returned count.
"""