# LeetCode Problem 26: Remove Duplicates from Sorted Array

# Given an integer array 'nums' sorted in non-decreasing order, remove the duplicates in-place such that 
#   each unique element appears only once. The relative order of the elements should be kept the same.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # leftPtr will point at the 
        # Number at zeroth index will never move, so start at index 1
        leftPtr = 1


        # As we loop through array (only once), rightPtr is the current position
        for rightPtr in range(1, len(nums)):

            if(nums[rightPtr] != nums[rightPtr - 1]):

                # , then increment the leftPtr position
                nums[leftPtr] = nums[rightPtr]
                leftPtr += 1

        # Time complexity is O(n * 2), which is amortized to O(n)
        return leftPtr
