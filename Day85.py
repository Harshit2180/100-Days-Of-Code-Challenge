# Question Link
# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)


"""
I started by initializing an empty stack to process the characters in the string s. As I iterated through each character in the string, if the character was an asterisk (*), I removed the last character from the stack. If it was any other character, I added it to the stack. After processing the entire string, I joined the remaining characters in the stack to form the final result and returned it.
"""