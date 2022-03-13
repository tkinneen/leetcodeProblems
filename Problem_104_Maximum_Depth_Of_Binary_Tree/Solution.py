# LeetCode Problem 104: Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path 
#    from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Time complexity is O(n) as is space complexity, because we recursively
        #    traverse the entire tree node

        # Base case for recursion - return 0 for null nodes
        if not root:
            return 0

        print(str(root.val) + " ===============open")
        print("Current node: " + str(root.val))
        # Recursively calculate the deepest child node, add 1 for the current node's
        #    level, then return the combined value to the next node up the tree
        returning = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        print("node " + str(root.val) + " returning: " + str(returning))
        print(str(root.val) + " ===============close")


        return returning

        
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
