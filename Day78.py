# Question Link
# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        RowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        RowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if RowZero:
            for c in range(COLS):
                matrix[0][c] = 0

"""
I began by determining the number of rows and columns in the matrix, storing them in ROWS and COLS. I also initialized a boolean variable RowZero to keep track of whether the first row contains any zeros. Next, I iterated through each element in the matrix. If I encountered a zero, I marked the corresponding first element of that row and column as zero. For the first row, I used the RowZero flag to remember if any zeros were found. After marking, I processed the rest of the matrix, starting from the second row and column. If the first element of a row or column was zero, I set the corresponding element in the matrix to zero. Finally, I checked if the top-left element of the matrix was zero. If it was, I set the entire first column to zero. Additionally, if RowZero was true, I set the entire first row to zero. This ensures that all necessary rows and columns are set to zero as required.
"""

