# Question Link
# https://leetcode.com/problems/rotate-list/description/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        LastElement = head
        length = 1
        while LastElement.next:
            LastElement = LastElement.next
            length += 1

        k = k % length
        LastElement.next = head
        TempNode = head
        for i in range( length - k - 1 ):
            TempNode = TempNode.next
        
        answer = TempNode.next
        TempNode.next = None
        
        return answer
    
"""
First, I checked if the input head was None, if it was, the function returned None immediately. Otherwise, I traversed the list to find the last node and calculate the length of the linked list. After determining the length, I used the modulo operation to handle cases where k was larger than the list's length, since rotating by the length of the list returns the same list. I then connected the last node to the head, forming a circular linked list. Next, I used a temporary node to traverse the list up to the point where the rotation should occur. This required moving length - k - 1 steps from the head to reach the new tail of the rotated list. I updated the next pointer of this new tail to None to break the circular link and return the new head of the rotated list.
"""