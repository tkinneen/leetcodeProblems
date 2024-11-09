# LeetCode Problem 230: Kth Smallest Element in a Binary Search Tree
#
# Given the root of a binary search tree, and an integer k, return the kth 
#    smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time: O(n) in the worst case
        # Space: O(h), where h is the height of the tree (O(log n) for balanced, O(n) for skewed)

        # self variables can be used as globals within leetcode Solution classes
        self.k = k
        self.result = None

        def dfs(node):

            # Recursion base case
            if not node:
                return
            
            # In-order traversal, so start with left
            dfs(node.left)
            
            # All left children have recursively been processed
            # Process the current node
            self.k -= 1

            # Perform a check here to see if we've reached the Kth node
            # Checking and returning here saves potenial unnecessary work
            #    of processing the right subtree
            if self.k == 0:
                self.result = node.val
                return
            
            # Now process the right chisubtreeldren
            dfs(node.right)
        
        # Kick off recursion; we will have the answer when this returns
        dfs(root)

        return self.result