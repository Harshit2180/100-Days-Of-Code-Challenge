# Question Link
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        characters = {"2": "abc", 
                      "3": "def",
                      "4": "ghi", 
                      "5": "jkl", 
                      "6": "mno", 
                      "7": "pqrs", 
                      "8": "tuv", 
                      "9": "wxyz"}

        def backtrack(i, CurStr):
            if len(CurStr) == len(digits):
                res.append(CurStr)
                return
            
            for c in characters[digits[i]]:
                backtrack(i + 1, CurStr + c)

        if digits:
            backtrack(0, "")
        
        return res

"""
I began by defining a result list, res, to store all the possible letter combinations. I also created a dictionary, characters, that maps each digit from 2 to 9 to its corresponding letters on a phone keypad. I then defined a recursive function, backtrack, which takes the current index i and the current string CurStr as arguments. The backtrack function first checks if the length of CurStr matches the length of the input digits. If it does, it means a valid combination has been formed and it is added to res. If not, I iterate over the possible characters for the current digit and recursively call backtrack with the next index and the updated string. Before starting the recursion, I checked if digits is not empty. If it isn't, I initiated the backtrack function starting from index 0 with an empty string. Finally, I returned the res list, which contains all the possible combinations.
"""