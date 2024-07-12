# Question Link
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root.left is None:
            return 1 + self.minDepth(root.right)

        if root.right is None:
            return 1 + self.minDepth(root.left)

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + min(left, right)
    
"""
First, I checked if the root of the tree is None. If it is, I return 0 because the tree is empty. If the root node has no left child, I return 1 plus the minimum depth of the right subtree. Similarly, if the root node has no right child, I return 1 plus the minimum depth of the left subtree. If both children exist, I recursively find the minimum depth of both the left and right subtrees. I then return 1 plus the smaller of these two depths. This way, I ensure that I calculate the minimum depth of the binary tree.
"""