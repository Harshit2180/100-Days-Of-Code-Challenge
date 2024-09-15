# Question Link
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while True:
            while cur:
                stack.append(cur)
                cur = cur.left

            if not stack:
                break

            node = stack.pop()
            k -= 1

            if  k == 0:
                return node.val

            cur = node.right


"""
I started by initializing an empty list called stack to help simulate in-order traversal and a variable cur pointing to the root of the tree. The goal is to traverse the tree in-order (left, root, right) to find the kth smallest element. I used a while True loop to handle this. First, I explored the leftmost subtree by continuously moving cur to its left child and adding nodes to the stack. Once I reached the leftmost node, I checked if the stack was empty, indicating the traversal is complete. If not, I popped the top node from the stack and decremented k. If k becomes 0, I returned the value of the current node, as it's the kth smallest element. Finally, I moved cur to the right child of the popped node to continue the in-order traversal.
"""