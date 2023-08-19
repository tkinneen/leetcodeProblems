# LeetCode Problem 019: Remove Nth Node From End of List
#
# Given the head of a linked list, remove the nth node from the end of the 
#    list and return its head.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Time complexity: O(n) - potentially the entire list must be traversed
        # Memory complexity: O(1)

        # 
        dummyNode = ListNode(0, head)
        leftPtr = dummyNode
        rightPtr = head

        # Step our right pointer down the list n times, spacing them appropriately
        while n > 0 and rightPtr: 
            rightPtr = rightPtr.next
            n -= 1
        
        # The left ptr starts at a dummy node BEFORE the first node in the list. 
        #    So it preceeds our right pointer by n+1 spaces.  If we walk both 
        #    pointers in sync one step at a time until the right ptr exceeds the
        #    last node in the list, the left pointer will reference the node directly
        #    before the nth node we want to remove. 
        while rightPtr:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next

        # To remove the nth node, update the 'next' value of the node left ptr references
        #    to two nodes down the list, essentially skipping the node we want to remove
        leftPtr.next = leftPtr.next.next
        
        # The dummy node's next value is still referencing the first node in the list, so return that
        return dummyNode.next