# LeetCode Problem 141: Linked List Cycle
# Given head, the head of a linked list, determine if the linked list 
#    has a cycle in it.

# There is a cycle in a linked list if there is some node in the list 
#    that can be reached again by continuously following the next pointer. 
#    Internally, pos is used to denote the index of the node that tail's 
#    next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # We use the "tortise and hare" algorithm here to solve the problem 
        #    with O(n) time complexity and O(1) space complexity 

        # Create a fast and slow pointer at the head of the linked list
        slowPtr = fastPtr = head

        # Continue looping until the end of the list is reached
        while fastPtr and fastPtr.next:
            
            # The slow pointer only moves one node at a time
            slowPtr = slowPtr.next
            
            # The fast pointer moves two nodes at a time
            fastPtr = fastPtr.next.next
            
            # If the linked list is a circuit, eventually the fast ptr will 
            #    catch up with the slow, and the ptrs will be on the same node
            if slowPtr == fastPtr:
                return True

        # If the list ends with no circuit, return False
        return False
