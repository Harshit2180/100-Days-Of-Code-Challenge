# Question Link
# https://leetcode.com/problems/course-schedule/description/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        PreReq = {i:[] for i in range(numCourses)}

        for courses, pre in prerequisites:
            PreReq[courses].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if PreReq[course] == []:
                return True
            
            visited.add(course)
            for pre in PreReq[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            PreReq[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    
"""
I started by setting up a dictionary called PreReq where each course maps to its list of prerequisites. I filled this dictionary using the prerequisites list. I then made a set called visited to keep track of courses we're currently checking to avoid loops. I defined a recursive function dfs to check if a course can be completed. The function checks if the course is already being visited, if the course has no prerequisites, and processes its prerequisites recursively. If any prerequisites cannot be completed, the function returns False. Finally, I used this function on each course. If any course can't be completed, I returned False. If all courses can be completed, I returned True.
"""