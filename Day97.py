# Question Link
# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
    

"""
I started by using three dictionaries to track the numbers present in each row, column, and 3x3 square on the Sudoku board. The keys of these dictionaries were the row indices for rows, the column indices for cols, and a tuple representing the square's location for squares. Each value was a set, storing the numbers seen in the corresponding row, column, or square. As I iterated through each cell in the 9x9 board, if I encountered a ".", I skipped the cell. Otherwise, I checked whether the current number was already present in its respective row, column, or square. If it was, the board would not be valid, so I returned False. If no conflicts were found after scanning the board, I returned True, indicating that the board followed the Sudoku rules.
"""