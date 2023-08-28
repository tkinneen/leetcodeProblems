# LeetCode Problem 102: Binary Tree Level Order Traversal
#
# Given the root of a binary tree, return the level order traversal of its 
#    nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Time complexity is O(n) as the entire binary tree must be traversed
        # Space complexity is O(n/2), or the largest possible level of a binary 
        #    tree, amoritzed to O(n)

        # This result array will contain a collection of subarrays, each 
        #    collecting all values at a specific level
        result = []

        # BFS processes nodes in the order they were added. We can use a 
        #    deque to add nodes to the array and pop from the left 
        q = deque()
        q.append(root)

        # Loop as long as at least one node exists in the queue. Each 
        #    iteration will clear out all nodes at the current level, but
        #    will append all its children to the queue for the next loop
        while q:

            # Get the current length of the queue - this dictates how many 
            #    nodes exist at the current level
            qLength = len(q)
            
            # This array will collect all values of nodes at the current level
            level = []

            # Process nodes from the current level in the order they were added to the q
            for i in range(qLength):
                curNode = q.popleft()
                
                # Check that the node is not null, then append its value to 
                #    this level's result array. Finally add both of its 
                #    children to the deque for the next loop iteration
                if curNode: 
                    level.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)
            
            # Append current level's value array to the result array
            #    it has any)
            if level:
                result.append(level)

        # All nodes in the tree have been traversed, return the result        
        return result

        