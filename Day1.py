class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result

""" 
Approach: To generate Pascal's Triangle, I started with [1] for the base case. For each new row, I appended 0s to both ends of the previous row and then summed adjacent pairs to form the new row. After this, I appended the new row to the result array.
"""