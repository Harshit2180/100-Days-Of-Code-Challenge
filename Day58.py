# Question Link
# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if ((r < 0 or c < 0) or 
                (r >= rows or c >= cols) or
                (word[i] != board[r][c]) or
                ((r,c) in path)):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
    
"""
I started by determining the number of rows and columns in the board and initializing an empty set path to keep track of the cells I have visited during my search. I defined a recursive function dfs that takes the current row, column, and the current index in the word. The function checks if I've found the entire word. If i equals the length of the word, it means I have matched all characters, so it returns True. The function also checks for invalid conditions: if the current position is out of bounds, if the character in the board does not match the current character in the word, or if the cell has already been visited. If any of these conditions are met, it returns False. If none of the invalid conditions apply, the function marks the current cell as visited and recursively explores all four possible directions (up, down, left, right). After exploring, it backtracks by removing the cell from the path. Finally, I loop through each cell in the board, calling dfs from each starting position. If dfs returns True for any starting position, I return True. If no valid path is found after checking all cells, I return False.
"""