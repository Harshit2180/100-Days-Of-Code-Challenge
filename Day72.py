# Question Link
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        dummy = ListNode(0)
        prev = dummy

        SumNodes = 0
        while temp:
            if temp.val == 0:
                prev.next = ListNode(SumNodes)
                SumNodes = 0
                prev = prev.next
            else:
                SumNodes += temp.val
            
            temp = temp.next

        return dummy.next
    
"""
I started by creating a dummy node to serve as a placeholder at the beginning of the new linked list. The prev pointer was initialized to this dummy node, and a variable SumNodes was initialized to keep track of the sum of node values between two zeros. I then used a while loop to traverse the linked list starting from the node after the head. For each node, I checked if its value was 0. If it was, I created a new node with the value of SumNodes, added it to the new list, reset SumNodes to 0, and moved the prev pointer to this new node. If the value was not 0, I added the node's value to SumNodes. Finally, after traversing all the nodes, I returned the linked list starting from the node after the dummy node.
"""