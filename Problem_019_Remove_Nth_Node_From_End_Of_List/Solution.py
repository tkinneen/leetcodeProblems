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

        # Brute force solution loops through the array of nodes, merging in each new list.
        #    This is a lot of repeated work and from-the-beginning re-iteration, a time 
        #    complexity of O(k * n)
        #
        # Best time complexity is O(n log k), where log k is the number of times the list 
        #    can be chopped in half. 

        # Protection for null or empty list array
        if not lists or len(lists) == 0:
            return None
        
        # Loop until there is only one node remaining. 12 lists will become 6, 
        #    6 will become 3, 3 will become 2, and 2 will become 1. The passed-in
        #    lists array gets updated after each iteration
        while len(lists) > 1:
            
            # Accumulates merged lists after each for loop iteration
            mergedLists = []
            
            # Iterate through the current state of the lists array, stepping two at a time.
            #    Each time throguh the for loop, two lists get merged, and that merged list
            #    is added to the mergedLists array, which overwrites the lists array each 
            #    while loop iteration 
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]
                
                # Below protection is necessary because odd-lengthed lists will throw
                #    an error at the last iteration. In that scenario, set list 2 to null 
                #    as the helper function can handle that
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Call the helper function that simply mergers 2 lists, then append the result to the merged array
                mergedLists.append(self.mergeTwoLists(l1, l2))
            
            # Update the array of lists, now further reduced
            lists = mergedLists

        # Return the only list that remains in the array
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