# LeetCode Problem 206: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return
#    the reversed list.

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # This solution is O(n) time complexity, and O(1) space complexity, 
        #   because we're using only pointers and not data structures

        # Set opposite direction "next" pointer
        prev = None
        # Current pointer is the passed-in head
        current = head

        # Loop until the node is null
        while current:
            # Save "next" node in original direction while we shuffle current node's pointers
            next = current.next
            
            # Current node's "next" pointer moving the opposite way 
            current.next = prev
            
            # prev gets shifted to the current node
            prev = current
            
            # the current node is shifted to the next node in the original direction, 
            #    and the process repeats
            current = next

        # Set current ptr to head of newly-reversed list
        current = prev

        return current