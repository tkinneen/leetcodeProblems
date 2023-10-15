# LeetCode Problem 124: Binary Tree Maximum Path Sum
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent 
#    nodes in the sequence has an edge connecting them. A node can only appear 
#    in the sequence at most once. Note that the path does not need to pass 
#    through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Time complexity: O(n) as we have to traverse every node once
        # Memory complexity: O(h) (the height of the tree, usually log n if it's balanced)

        # Initialize to the value of root, but this will potentially be updated
        #    each iteration of our recursive dfs function
        maxPathSum = root.val

        # Returns the max path sum of the current node WITHOUT splitting
        def dfs(root):

            # nonlocal allows us to access a global variable inside the dfs function
            nonlocal maxPathSum

            # Base case = return 0 for null branches
            if not root:
                print("null return")
                return 0
                        
            # Run a recursive check on both the left and right branches of the 
            #    current node, which yeilds the non-split max sum UP to this point
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If either of the above sums are negative, set the value to 0 to 
            #    essentially "reset" with the current node's value
            leftmax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Calculate the max path sum WITH a split, and update if it's the 
            #    largest we've seen yet 
            maxPathSum = max(maxPathSum, root.val + leftMax + rightMax)

            # Return the non-split max sum of the current node, consisting of 
            #    the current node's value summed with its largest non-split child
            return root.val + max(leftMax, rightMax)
        
        # Kick off the recursive depth first search
        dfs(root)

        # Return the result, which gets populated by above search
        return maxPathSum