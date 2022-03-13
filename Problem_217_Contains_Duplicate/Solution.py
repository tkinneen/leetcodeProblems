# LeetCode Problem 217: Contains Duplicate
# Given an integer array nums, return true if any value appears at least 
#    twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create a dictionary to collect already-see number for fast lookup
        numsAlreadySeen = {}
        
        # Loop through all numbers and check dict, return immediately when dupe is found
        for currentNum in nums:
            if currentNum in numsAlreadySeen:
                return True
            else:
                # If current number is not found, add it to the dictionary
                numsAlreadySeen[currentNum] = 0
        
        # Return false if there are no inputs in the test array
        return False