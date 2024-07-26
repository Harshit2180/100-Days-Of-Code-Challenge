# Question Link
# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
"""
I started by making a dummy node and setting curr to point to it. I also set up a carry variable to manage any extra value from adding digits. Next, I created a loop that continued as long as nodes were left in l1 or l2, or if there was a carry. Inside the loop, I got the values from the current nodes in l1 and l2, using 0 if a list was empty. I added these values and the carry, then updated the carry to the tens place and the current digit to the units place. I created a new node with this digit and attached it to curr. After that, I moved curr to this new node and moved l1 and l2 if they had more nodes. Finally, I returned the node following the dummy, which is the head of the resulting linked list.
"""