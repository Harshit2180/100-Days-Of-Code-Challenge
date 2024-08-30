# Question Link
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
"""
I started by setting cur to the root of the binary search tree. Using a while loop, I checked the value of cur against the values of p and q. If both p and q had values greater than the current value, it meant both nodes were in the right subtree, so I moved cur to the right child. If both p and q had values less than the current value, it meant both nodes were in the left subtree, so I moved cur to the left child. If neither of these conditions was true, it indicated that the current node cur was the lowest common ancestor of p and q. I then returned cur as the result.
"""