# Question Link:
# https://leetcode.com/problems/valid-boomerang/description/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

        return area != 0
    
"""
First, I extracted the coordinates of the three points from the points list. The coordinates of the first point are x1 and y1, the coordinates of the second point are x2 and y2, and the coordinates of the third point are x3 and y3. Then, I calculated the area of the triangle using a formula. Finally, I checked if the area is not equal to zero. If the area is not zero, the points form a boomerang, and I return true; otherwise, I return false.
"""