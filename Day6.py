# Question Link:
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        elif val < root.val:
            return self.searchBST(root.left, val) # (4,2) (2,2)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root
        
"""
In this code, I am searching for a value in a binary search tree. If the root is None, I return None because the value isn't found. If the value I'm looking for is less than the root's value, I search the left subtree. If the value is greater, I search the right subtree. I search the values by recursively calling the function. If the value matches the root's value, I return the root node.
"""