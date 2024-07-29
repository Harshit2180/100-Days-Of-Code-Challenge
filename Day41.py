# Question Link
# https://leetcode.com/problems/subtree-of-another-tree/description/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
    
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
            
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        return False    
    
"""
First, in the isSubtree function, I checked if subRoot is empty. If it is, I returned True because an empty tree is always a subtree. If root is empty but subRoot isn't, I returned False because a non-empty subRoot can't be part of an empty root. Next, I used the sameTree function to see if the current part of root matches subRoot. If they match, I returned True. If not, I looked at the left and right parts of root to see if subRoot matches either of those. The sameTree function checks if two trees are identical. It compares their root values and their left and right children to see if everything matches. If both trees are exactly the same, it returns True; otherwise, it returns False.
"""