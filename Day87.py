# Question Link
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next
    

"""
I began by creating a dummy node that points to the head of the linked list. This dummy node helps handle edge cases where the head itself needs to be swapped. I also used a prev pointer to keep track of the node before the current pair of nodes being swapped. The loop continues as long as there are at least two nodes to swap. In each iteration, I assigned the current node to first and the node immediately after it to second. To swap them, I connected the node before the pair (prev) to the second node, making it the new start of the pair. Then, I linked the first node to the node following the second, and the second node back to the first to complete the swap. After the swap, I updated prev to point to the first node (now second in the swapped pair), and I advanced the head pointer to move on to the next pair of nodes. Finally, I returned the node after the dummy node, which is the new head of the linked list.
"""