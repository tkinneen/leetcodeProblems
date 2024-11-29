# LeetCode Problem 235: Lowest Common Ancestor of a Binary Search Tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) 
#    node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
#    is defined between two nodes p and q as the lowest node in T that has both 
#    p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import Optional

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

        # Time: O(h) - explores the height of the tree in worst case
        # Space: O(1) - simply tracks the current node regardless of tree size

        # Start at the root; it will always be a common ancestor of every node in the tree, though not necessarily the lowest
        curNode = root

        # Loop until the solution is found
        while curNode:
            # Both p and q are greater than the current node, so both reside in the right subtree.
            #   Shift current node to the right child and continue search
            if p.val > curNode.val and q.val > curNode.val:
                curNode = curNode.right
            # Both p and q are less than the current node, so both reside in the left subtree.
            #   Shift current node to the left child and continue search
            elif p.val < curNode.val and q.val < curNode.val:
                curNode = curNode.left
            # p and q reside in separate subtrees, so the current node is the lowest possible common ancestor (the split)
            else:
                return curNode