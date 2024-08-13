# Question Link
# https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldList = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            OldList[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = OldList[cur]
            copy.next = OldList[cur.next]
            copy.random = OldList[cur.random]
            cur = cur.next

        return OldList[head]
    
"""
I started by creating a dictionary called OldList to map the original nodes to their copies. I set an initial entry for None to handle the edge case of null pointers. Then, I traversed the original list with cur, creating a copy of each node and storing it in the dictionary. Each original node was mapped to its new copy. After this, cur was reset to the head of the original list to set up the next and random pointers for each copied node. In the second pass, I updated each copied node’s next and random pointers using the OldList dictionary to look up the corresponding copies. Finally, I returned the copy of the head node, which is the start of the new list with all nodes correctly copied and linked.
"""