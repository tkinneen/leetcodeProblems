# LeetCode Problem 572: Subtree of Another Tree
#
# Given the roots of two binary trees root and subRoot, return true if there 
#    is a subtree of root with the same structure and node values of subRoot 
#   and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree 
#    and all of this node's descendants. The tree tree could also be considered 
#    as a subtree of itself.

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Time Complexity: O(numNodesInRoot * numNodesInSubroot)
        # Memory Complexity O(m):
        # In the worst case, if the main tree is highly unbalanced (e.g., a 
        #    skewed tree), the stack space can be O(m) due to the recursive 
        #    calls, where 'm' is the number of nodes in the main tree

        # If subRoot is null, it is a valid subtree by default
        if not subRoot:
            return True
        
        # If root is null and subRoot isn't, subRoot cannot be a valid subtree
        # We know subRoot is not null here because of check above  
        if not root:
            return False
        
        # Perform a check on the current node to see if it and its children are
        #    a match for the subtree
        if self.sameTree(root, subRoot):
            return True
        
        # If it's NOT a match, recurse into bothe the left and right children, 
        #    using the next node down as the new root to compare
        return(self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        
    def sameTree(self, s, t):

        # Both lists are empty, so technically are the same tree
        if not s and not t:
            return True
        
        # Current node is valid, must perform recursive compare on their children
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

        # If neither of the above conditions execute, it means one of the 
        #    trees is empty and one is non-empty, hence not the same tree
        return False