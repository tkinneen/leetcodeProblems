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
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Time complexity is O(n) as we have to traverse the entire tree
        # Space complexity is also worst case O(n) if it's not a balanced tree

        # Recursive Depth First Search (DFS) Implementation
        def RecursiveDFS(root):
            
            # Base case for recursion - return 0 for null nodes
            if not root:
                return 0
            
            # Recursively calculate the deepest child node. Each node will take the 
            #    largetst value returned by its own children, then add 1 to represent
            #    its own depth and return that to its parent
            currentMax = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

            return currentMax
        
        # Breadth First Search (BFS) Implementation
        def BreadthFirstSearch(root):
            
            # Base case for recursion
            if not root:
                return 0
            
            # St
            level = 0
            
            # Deque allows us to efficiently pop from either the left or right of queue
            queue = deque([root])
            
            # Loop as long as nodes exist in the deque
            while queue:
                # 
                for i in range(len(queue)):
                    # Pop from the deque in the order the nodes were added
                    node = queue.popleft()
                    # Append both child nodes to the deque, regardless of whether they are Null
                    queue.append(node.left)
                    queue.append(node.right)
                # Increment the level after each wave of nodes
                level += 1
            return level
            
        # Iterative Depth First Search (DFS) Implementation
        def iterativeDFS(root):
            
            # Base case for recursion
            if not root:
                return 0
            
            # Store the node as well as its depth in the stack
            stack = [[root, 1]]
            
            # Continually increment the max depth 
            maxDepth = 1

            # Continue looping while there are nodes in the stack
            while stack:
                
                # Grabs the last-added node and its depth from the stack
                node, depth = stack.pop()    
            
                if node:
                    # Updates the max depth val if current node's depth is greater
                    maxDepth = max(maxDepth, depth)
                    # Appends the children of the current node to the stack (they may be null)
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])

            # Return the maxDepth when there are no more nodes in the stack
            return maxDepth

        # 3 different implementations, all return the same answer
        return RecursiveDFS(root)
        #return BreadthFirstSearch(root)
        #return iterativeDFS(root)           

