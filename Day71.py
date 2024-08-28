# Question Link
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, same, greater = [], [], []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                same.append(i)
            else:
                greater.append(i)
        
        return less + same + greater


"""
 I started by initializing three lists less, same, and greater. These lists will store elements from the input list nums based on their comparison with a pivot value. I then iterated through each element in nums. For each element, I compared it with the pivot. If the element was less than the pivot, I added it to the less list. If it was equal to the pivot, I added it to the same list. If it was greater than the pivot, I added it to the greater list. Finally, I combined the less, same, and greater lists in that order and returned the result.
"""