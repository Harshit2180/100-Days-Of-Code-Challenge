# Question Link
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {0: 0, 1: 0}
        res = len(students)

        for i in students:
            count[i] += 1
                
        for j in sandwiches:
            if count[j] > 0:
                res -= 1        
                count[j] -= 1    
            else:
                return res  
        return res

"""
First, I create a dictionary count to track the number of students preferring each type of sandwich, initializing both to 0. I set res to the number of students. I then loop through the students list to update their preferences in count. Next, I loop through the sandwiches list. If there are students who prefer the current sandwich, I decrement res and the corresponding count in count. If no students prefer the current sandwich, I return res. Finally, I return res, which shows the number of students who can't be served.
"""