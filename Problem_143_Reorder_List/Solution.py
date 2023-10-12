# LeetCode Problem 143: Reorder List
#
# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may 
#    be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Time complexity: O(n) [amortized from O(2n) as we traverse the list twice]
        # Memory complexity: O(1) [we're using a fixed number of pointers and modifying passed-in list]

        # Set a fast and slow pointer at the 1st and 2nd positions of the list
        slowPtr, fastPtr = head, head.next

        print(f"initial slowPtr.val: {slowPtr.val}")
        print(f"initial fastPtr.val: {fastPtr.val}")

        # Loop through the entire list, stepping the slow ptr by 1 and the 
        #    fast ptr by 2 each iteration. On loop-end slowPtr is the midpoint
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
        # Start of the 2nd list (which we will now reverse)
        second = slowPtr.next
        
        # prev ptr will help us reverse "next" pointers (initialize to Null)
        previous = None

        # End 1st list after midpoint (essentilly chop original list in 2ff)
        slowPtr.next = None

        # Traverse the second half of the list, reversing pointers
        while second:
            
            # Preserve link to the original next node
            temp = second.next

            # Reverses the link
            second.next = previous

            # Previous becomes the current node 
            previous = second

            # Current becomes the next node in the original order
            second = temp
        
        # Create pointers to our two lists we must merge
        firstList, secondList = head, previous
        
        # Merge the two lists in place, yeilding the requested reorder
        while secondList:

            # Preserve the next pointer of both lists, as we will be re-arranging them
            temp1, temp2 = firstList.next, secondList.next
            
            # firstList's next pointer aims at current node in secondList 
            firstList.next = secondList

            # secondList's next pointer aims at what was originally firstList.next
            # Each loop we're essentially inserting a node from secondList between two nodes in firstList
            secondList.next = temp1

            # Progress to the next node of both lists in their original order 
            firstList, secondList = temp1, temp2

            # No need to return a value as we modified the linked list in-place