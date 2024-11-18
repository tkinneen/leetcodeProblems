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
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Time: O(n log k) 
        # Space: O(k)
        # Where n is the number of nodes across all lists, and k is the number 
        #   of sorted lists in the heap
        # Inserting each element into a heap takes O(log k) time

        # Heap is a specialized binary tree that always keeps the min value at the root
        #    node. The heapq library uses a list to simulate heap binary tree
        min_heap = []
        
        # Populate the heap by looping through every list and inserting the head node
        for idx, curList in enumerate(lists):
            # Only insert valid ListNodes
            if curList:
                # Pass in the array we're using as a heap, and a tuple that 
                #    contains the value we're sorting, the index so we don't 
                #    clash at duplicate values, and the reference to the associated
                #    node so we can access the next node as we process
                heapq.heappush(min_heap, (curList.val, idx, curList))
        
        # Create a dummy node from which we can begin merging
        # We will append each new node to the tail, and head will allow us to 
        #   get back to the front of the list once fully merged
        head = tail = ListNode()
        
        # Walk the heap until it's empty
        while min_heap:

            # Pop from the heap; this will be the lowest of all list values
            # Destructure each 3-item tuple that pops off
            curVal, idx, curNode = heapq.heappop(min_heap)
            
            # Create a new ListNode for the tuple we just popped and append it to 
            #    the output linked list
            tail.next = ListNode(curVal)

            # Walk the tail pointer to the new tail
            tail = tail.next
            
            # Walk the pointer of the list you just merged then put it back into the heap
            if curNode.next:
                heapq.heappush(min_heap, (curNode.next.val, idx, curNode.next))
        
        # List is fully merged but head points to the dummy node, so head.next
        #    gives you the actual head
        return head.next