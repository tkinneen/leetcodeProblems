# LeetCode Problem 217: Contains Duplicate
# Given an integer array nums, return true if any value appears at least 
#    twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create a dictionary to collect already-see number for fast lookup
        seenNums = set()
        
        # Loop through each num in input array and check set for duplicates. Return if dupe is found
        for curNum in nums:
            if curNum in seenNums:
                return True
            else:
                # If current number has not been seen, add it to the set
                seenNums.add(curNum)
        
        # No duplicated have been found
        return False