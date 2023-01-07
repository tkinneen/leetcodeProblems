# LeetCode Problem 104: Maximum Depth of Binary Tree
#
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path 
#    from the root node down to the farthest leaf node.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Time complexity is O(n) as the entire tree must be traversed
        # Space complexity is worst case O(n) if the tree isn't balanced

        # Recursive Depth First Search (DFS) Implementation
        def RecursiveDFS(root):
            
            # Base case for recursion - return 0 for null nodes
            if not root:
                return 0
            
            # Recursively calculate the deepest child node. Each node will take the 
            #    largetst value returned by its own children, then add 1 to represent
            #    its own depth and return that to its parent
            maxDepth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            return maxDepth
        
        # Breadth First Search (BFS) Implementation
        def BreadthFirstSearch(root):
            
            # Edge case if a null node is passed in
            if not root:
                return 0
            
            # Increment this value each time we move deeper into the tree
            maxDepth = 0
            
            # Deque allows us to efficiently pop from the left or right of a queue
            queue = deque([root])
            
            # Loop as long as nodes exist in the deque
            while queue:

                # If we do a second loop with a range of the current length of the queue, 
                #   it will go through all the nodes at the current level for each iteration.
                # So if all nodes have 2 children, iteration would be len 1, 2, 4, 8, 16, etc.
                for i in range(len(queue)):
                    
                    # Pop from the left 
                    node = queue.popleft()
                    
                    # Append both child nodes to the deque (if they exist)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                # Increment the level after each wave of nodes
                maxDepth += 1
            
            # When the entire tree has been traversed, return the deepest level that was acheived
            return maxDepth
            
        # Iterative Depth First Search (DFS) Implementation
        def iterativeDFS(root):
            
            # Edge case if a null node is passed in
            if not root:
                return 0
            
            # Store the node as well as its depth in the stack
            stack = [[root, 1]]
            
            # Continually increment the max depth 
            maxDepth = 0

            # Continue looping while there are nodes in the stack
            while stack:
                
                # Grabs the last-added node and its depth from the stack
                node, depth = stack.pop()

                # First check that the node is not Null
                if node:
                    # Updates the max depth val if the current node's depth is greater
                    maxDepth = max(maxDepth, depth)
                    
                    # Append the children of the current node to the stack, updating the depth as well
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])

            # When the entire tree has been traversed, return the deepest level that was acheived
            return maxDepth

        # 3 different implementations, all return the same answer
        #return RecursiveDFS(root)
        #return BreadthFirstSearch(root)
        return iterativeDFS(root)