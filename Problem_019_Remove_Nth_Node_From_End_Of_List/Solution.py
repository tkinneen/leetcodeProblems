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
        
        # Time complexity: O()
        # Memory complexity: O()

        # 
        dummyNode = ListNode(0, head)
        leftPtr = dummyNode
        rightPtr = head

        while n > 0 and rightPtr: 
            rightPtr = rightPtr.next
            n -= 1
        
        while rightPtr:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next

        leftPtr.next = leftPtr.next.next
        
        return dummyNode.next