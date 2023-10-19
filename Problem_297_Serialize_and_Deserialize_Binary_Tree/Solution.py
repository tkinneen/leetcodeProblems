# LeetCode Problem 297: Serialize and Deserialize Binary Tree
#
# Serialization is the process of converting a data structure or object into a 
#    sequence of bits so that it can be stored in a file or memory buffer, or 
#    transmitted across a network connection link to be reconstructed later in 
#    the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no 
#    restriction on how your serialization/deserialization algorithm should work. 
#    You just need to ensure that a binary tree can be serialized to a string and 
#    this string can be deserialized to the original tree structure.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Codec:

  # Converts a passed-in binary tree to a string of node values
  def serialize(self, root):
        
    # Each value will be added to this array (can be appended from within the 
    #    helper function)
    result = []
    
    # Implement a depth first search function that will traverse the entire 
    #    tree, updating the result at each iteration
    def dfs(curNode):
    
      # Base case for recursion: 
      if not curNode:
        result.append("Null")
        return
      
      # If the current node is valid, convert its value to a string and 
      #    append it to the result array
      result.append(str(curNode.val))
      
      # Continue recursion by performing a dfs on both of the current 
      #    node's children
      dfs(curNode.left)
      dfs(curNode.right)
    
    # Initiate recursion
    dfs(root)
    
    # Convert the result array to a single comma-delimited string
    return ",".join(result)

  # Converts a string of node values into a binary tree
  def deserialize(self, data):
  
    # Split the input string into an array we can easily traverse
    values = data.split(",")
    
    # Maintain an index position
    self.i = 0
    
    # Helper function that performs a depth first search of the entire tree
    def dfs():
      # Check the current index for the Null special case
      if values[self.i] == "Null":
        # Just increment the index and return, do not create a new node
        self.i += 1
        return None
      
      # Instantiate a new TreeNode with the current index value, first 
      #    converting from string to int
      curNode = TreeNode(int(values[self.i]))
      
      # Bump the index position
      self.i += 1
      
      # Continue recursion
      curNode.left = dfs()
      curNode.right = dfs()

      # Return the root node of the now fully-built tree
      return curNode
    
    # Initiate recursion, and return the root node that gets built up
    return dfs()