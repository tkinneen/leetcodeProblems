# LeetCode Problem 226: Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # This recursive swap operation must be performed on every node in the tree, 
        #    so we have O(n) time complexity and O(n) space complexity

        # Base case - recursion will cease when the current node is null
        if not root:
            return None
        
        # Flip the child nodes
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively call invertTree function on both children
        # This will continue until the base case at the beginning of this function is engaged
        self.invertTree(root.left)
        self.invertTree(root.right)

        # All nodes are now swapped, we can return the root
        return root
