# LeetCode Problem 153: Find Minimum in Rotated Sorted Array
#
# Given an integer array nums, find a subarray that has the largest product, and
#    return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# Suppose an array of length n sorted in ascending order is rotated between 1 
#    and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
#    in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum 
#    element of this array.
#
# You must write an algorithm that runs in O(log n) time.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # Edge case protections
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        
        # Set a pointer at each end of the array
        leftPtr, rightPtr = 0, len(nums) - 1

        # Loop until the two pointers meet
        while leftPtr < rightPtr:

            # Calculate midpoint between the two pointers
            # Divison floor operator (//) operator will make the midpoint of 
            #    arrays with an even number of elements err to the left
            midpoint = (leftPtr + rightPtr) // 2

            # We need to do a binary search for the pivot point of this sorted array.
            #    Each loop iteration will calculate the midpoint of the array portion 
            #    we're currently examining, then check the number at the midpoint 
            #    against the right pointer. This will tell which side is sorted, and 
            #    we will shift the pointers towards each other to further discard the 
            #    sorted portion

            # The number at the midpoint is greater than at the rightPtr, so the
            #    right half of the array is NOT in sorted order. The pivot resides there
            if nums[midpoint] > nums[rightPtr]:
                # If the mid is greater than the right we know it's not the pivot, so 
                #    shift the left pointer to EXCLUDE that value
                leftPtr = midpoint + 1
                
            # The number at the midpoint is less than the number at the rightPtr, so the
            #    left half of the array is sorted. This tells us the pivot is
            #    in in the other portion of the arraay, so shif the rightPtr to mid to
            #    "throw away" the already0-sorted data
            else:
                # If the mid element is less than the right element, it COULD be the pivot, 
                #    so we shift the right ptr to mid's current position
                rightPtr = midpoint
            
        return nums[leftPtr]