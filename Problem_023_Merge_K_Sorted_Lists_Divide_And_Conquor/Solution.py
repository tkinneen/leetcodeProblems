# LeetCode Problem 023: Merge k Sorted Lists
#
# You are given an array of k linked-lists lists, each linked-list is sorted 
#    in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Time: O(N log k) ...where N is the total number of nodes across all lists,
        #    and k is the total number of lists
        # Space: O(k) because of the array space required at the beginning before merging 

        # If lists is null or empty, we're done already
        if not lists or len(lists) == 0:
            return None
        
        # Loop until there is only one list remaining
        # 12 lists -> 6 -> 3 -> 2 -> 1
        while len(lists) > 1:
            
            # While we're in the process of merging lists within the for loop,
            #    accumulate them in this array
            mergedLists = []
            
            # Iterate through the current state of the lists array, stepping two at a time
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]
                
                # Set list 2, protecting against odd-lengthed list arrays
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Call the helper function that simply mergers 2 lists, then append the result to the merged array
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Update the now-halved array of lists
            lists = mergedLists

        # Return the fully merged ListNode, the only list that remains
        return lists[0]

    # Helper function that simply merges two sorted lists (this was LC Problem 21)
    def mergeTwoLists(self, l1, l2):
        
        # The tail is the pointer where the merges take place, and the dummyNode 
        #    provides a bookmark to get back to the head after the merge has 
        #    completed
        dummyNode = tail = ListNode()

        # As long as there are two values to compare, merge the lower of the two
        #    current values and march the tail 
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # When one of the lists has been exhausted, append the rest of the 
        #    remaining list to the merged output list
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        # Increment the dummy node, returning the head of the now-sorted list
        return dummyNode.next