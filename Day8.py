#Question Link
# https://leetcode.com/problems/binary-watch/

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res

"""
I created an empty list called res. Then, I used two loops: one to go through the hours from 0 to 11, and one to go through the minutes from 0 to 59. For each hour and minute, I changed them to binary and counted the 1s. If the total number of 1s was equal to turnedOn, I added the time to res in the format h:mm, making sure the minutes always had two digits. After going through all the times, I returned the res list.
"""
