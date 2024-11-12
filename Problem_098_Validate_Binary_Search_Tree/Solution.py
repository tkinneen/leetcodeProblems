# LeetCode Problem 098: Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Time: O(n)
        # Space: O(h) or height of tree...n in worst case log n for balanced

        # Create helper function, called recursively to check that each node's value is 
        #    within acceptable bounds
        def checkValidity(node, leftBound, rightBound):
            
            # An empty node is still valid
            if not node:
                return True
            
            # Ensure current node's value isn't outside legal bounds
            if not (node.val > leftBound and node.val < rightBound):
                return False

            # Recursively check both children of the current node, using the current node's value
            #    as the upper bound for the left child, and the lower bound for the right child.
            return(checkValidity(node.left, leftBound, node.val) 
                and checkValidity(node.right, node.val, rightBound ))

        # This call starts the recursive check using initial bounds 
        return checkValidity(root, float("-inf"), float("inf"))
