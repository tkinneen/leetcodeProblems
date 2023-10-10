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

from typing import List, Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Time complexity: O(n) [amortized from O(2n) as we traverse the list twice]
        # Memory complexity: O(1) [we're using a fixed number of pointers and modifying passed-in list]

        # Set a fast and slow pointer at the first and second positions of the list
        slowPtr, fastPtr = head, head.next

        print(f"initial slowPtr.val: {slowPtr.val}")
        print(f"initial fastPtr.val: {fastPtr.val}")

        # Loop through the entire list, stepping the slow ptr by 1 and the 
        #    fast ptr by 2 each iteration
        # Odd-length lists the slow ptr will end at the midpoint, and even-length
        #    lists it will err left of center
        # Note: fast ptr ends on the last node of even-length lista
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
        # 
        second = slowPtr.next
        
        # previous will 
        previous = None

        # This will chop off the second half of the original list
        slowPtr.next = None

        # Traverse the second half of the list, reversing next ptrs
        while second:
            
            # Preserve link to the original next node
            temp = second.next

            # Reverses the link
            second.next = previous

            # Previous becomes the current node 
            previous = second

            # Current becomes the next node in the original order
            second = temp
        
        print(f"previous after reversal: {previous.val}")

        # These are the two lists we must merge to get our desired re-roder. secondList is the second half of the input list, reversed 
        # odd-length lists will always have one more node than secondList)
        firstList, secondList = head, previous
        
        # Finally, merge secondList (which is the second half of the original list, reversed) into 
        #    firstList. This gives us the new order requited by the solution
        # Loop while secondList is not null, as it will always be shorter
        while secondList:

            # Preserve the next pointer in both lists, as we will be breaking them
            temp1, temp2 = firstList.next, secondList.next
            
            # Take the current node of secondList and insert it into the next position of firstList
            firstList.next = secondList

            # , and makes it a contiguous list
            secondList.next = temp1

            # Make the current node of both lists the next 
            firstList, secondList = temp1, temp2
        
        # 
        return None