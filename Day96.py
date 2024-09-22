# Question Link
# https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, s: str) -> bool:
        LeftMin, LeftMax = 0, 0

        for i in s:
            if i == "(":
                LeftMin, LeftMax = LeftMin + 1, LeftMax + 1
            elif i == ")":
                LeftMin, LeftMax = LeftMin - 1, LeftMax - 1
            else:
                LeftMin, LeftMax = LeftMin - 1, LeftMax + 1

            if LeftMax < 0:
                return False

            if LeftMin < 0:
                LeftMin = 0

        return LeftMin == 0   
    

"""
I began by initializing two variables, LeftMin and LeftMax, both set to zero. These will help track the range of possible open parentheses as I iterate through the string. As I processed each character in the string, I updated these variables based on the type of character encountered. When I found an opening parenthesis "(", both LeftMin and LeftMax were incremented. For a closing parenthesis ")", both were decremented. When I encountered an asterisk "*", I decreased LeftMin by one (since it could be a closing parenthesis) and increased LeftMax by one (since it could be an opening parenthesis). Throughout this process, I checked if LeftMax became negative. If it did, it indicated that there were too many closing parentheses, so I returned False. Additionally, if LeftMin dropped below zero, I reset it to zero, as this scenario still allows for a valid configuration. Finally, I returned True if LeftMin was zero at the end, indicating that all parentheses could be matched correctly.
"""