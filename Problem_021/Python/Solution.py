# LeetCode Problem 21: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by 
#   splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Instantiate the answer list with head and tail pointers on a dummy node
        head = tail = ListNode()

        # While nodes exist in both lists, compare the two current values and append 
        #   the lower one to the answer list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # If one list runs out of nodes, append the rest of the remaining list to the
        #   answer's tail.  This works because both lists are already ordered.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Head was pointing to a dummy value, so returning head.next
        #   will be the first node in our answer
        return head.next
