class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n

        if k == 0:
            print(res)
        elif k > 0:
            for i in range(n):
                for j in range(1, k+1):
                    res[i] = res[i] + code[(i+j)%n]
        else:
            for i in range(n):
                for j in range(-1, k-1, -1):
                    index = (i+j)%n
                    if index < 0:
                        index = n + index
                    res[i] = res[i] + code[index]
            
        return res
    
"""
In this code, I made a list called res that is the same length as code and filled it with zeros. If k is 0, I just print res. If k is positive, I go through each item in code and add the next k items to it, wrapping around if needed. If k is negative, I add the previous k items instead. Finally, I return the res list.
"""