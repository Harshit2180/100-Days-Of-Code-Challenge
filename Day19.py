# Question Link
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB

        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB
            if l2:
                l2 = l2.next
            else:
                l2 = headA
        return l1
    
"""
I set two pointers, l1 and l2, to the heads of the linked lists headA and headB respectively. I enter a while loop that continues until l1 and l2 are not the same node. If l1 is not null, I move it to the next node, otherwise, I reset it to headB. Similarly, if l2 is not null, I move it to the next node, otherwise, I reset it to headA. This way, the pointers eventually meet at the intersection node or at the end if there's no intersection. Finally, I return l1 which will be the intersection node or null if there is no intersection.
"""