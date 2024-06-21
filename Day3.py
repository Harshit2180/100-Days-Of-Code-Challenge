class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        left = head
        right = head.next

        while right:
            if left.val == right.val:
                left.next = right.next
                right = right.next
            else:
                left = left.next
                right = right.next
        return head
    
"""
To solve this problem, I first checked if the list is empty and returned it if so. If not, I set up two pointers: "left" starting at the head of the list and "right" at the next node. Using a while loop, I traversed the list, skipping duplicates by setting left.next to right.next when their values were equal, and moving "right" forward. If the values differed, I moved both pointers forward. This process continued until the "right" pointer reached the end of the list. Finally, I returned the list without duplicate values.
"""