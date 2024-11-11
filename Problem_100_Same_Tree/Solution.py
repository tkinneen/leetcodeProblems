# LeetCode Problem 100: Same Tree
#
# Given the roots of two binary trees p and q, write a function to check if
#    they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
#    and the nodes have the same value.

from typing import Optional

# Definition for a binary tree node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Time: O(n) since each node is visited exactly once
        # Space: O(h), where h is the height of the tree; skewed trees will be O(n), 
        #    balanced trees are O(log n)

        # If both nodes are null, recursive check is valid so just return True
        if not p and not q:
            return True
        # If only one node is null, or the values of the two nodes differ, entire result is False
        if not p or not q or p.val != q.val:
            return False

        # If we get here, both nodes are valid. Continue recursion
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
