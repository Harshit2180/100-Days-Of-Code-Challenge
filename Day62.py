# Question Link
# https://leetcode.com/problems/spiral-matrix/description/

left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []
        while (left < right and top < bottom):
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

"""
I started by setting the initial boundaries of the matrix: left and right for the sides, and top and bottom for the top and bottom edges. First, I moved across the top row from left to right and added each element to res. After finishing this row, I moved the top boundary down since that row was done. Next, I went down the rightmost column, adding each element to res, and then moved the right boundary left to mark that the column was processed. I then checked if there were still elements left to process. If not, I stopped the loop. If there were still elements left, I moved across the bottom row from right to left, adding each element to res, and then moved the bottom boundary up. Finally, I moved up the leftmost column, adding each element to res, and then moved the left boundary right. I repeated this process until all elements in the matrix were added to res in a spiral order. Then I returned the list res.
"""