# Question Link
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res
    
"""
I began by initializing an empty list res to store the values of nodes at each level. I also set up a queue using collections.deque and added the root node to it. I then entered a loop that continued while the queue was not empty. Inside the loop, I determined the number of nodes at the current level (qlen). I created an empty list level to hold the values of nodes at this level. For each node in the current level, I removed the node from the queue, added its value to level, and added its left and right children to the queue. After processing all nodes at the current level, I added the level list to res. Finally, I returned the res list, which contains the values of nodes grouped by their levels.
"""