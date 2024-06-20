class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        i = 0
        found = False

        while i < len(word) and not found:
            stack.append(word[i])
            if word[i] == ch:
                found = True
            i += 1
                
        if found == False:
            return word

        res= ""
        while stack:
            res += stack.pop()
        return (res + word[i:])
    
""" 
Approach: My approach was to add characters to a stack until the desired character was found. If it wasn't found, I returned the original word. If it was found, I set the "found" variable to True, then popped each character from the stack and added it to the string "res" until the stack was empty. Finally, I added the remaining characters of the word to "res" and returned this string.
"""