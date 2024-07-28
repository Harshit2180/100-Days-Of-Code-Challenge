# Question Link
# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row - 1

        while top <= bottom:
            row = (top + bottom)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False
        
        left = 0
        right = col - 1
        while left <= right:
            mid = (left + right)//2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
    
"""
I first determined the number of rows and columns in the matrix. I initialized top to 0 and bottom to the last row index. Using a binary search, I checked if the target is within the range of any row's values. If the target is greater than the last value of the current row, I moved the top pointer down. If the target is less than the first value, I moved the bottom pointer up. This loop continues until I narrow down to a potential row. If no valid row was found, I returned False. Otherwise, I used another binary search within the identified row to check if the target exists in that row. If found, I returned True; otherwise, I returned False.
"""