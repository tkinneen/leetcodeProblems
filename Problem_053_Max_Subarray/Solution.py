# LeetCode Problem 053: Max Subarray
#
# Given an integer array nums, find the contiguous subarray(containing at least
#    #one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Time and Memory complexity for this solution is O(n)
        # This is known as Kadane's Algorithm

        currentSum = maxSum = nums[0]

        # We already set currentSum to zeroth position, so loop thorugh the
        #    entire array from the first index position
        for currentNum in nums[1:]:

            # Update the currentSum for this iteration by adding the current
            #    array value to the running sum. But if this does not exceed
            #    the current array value alone, "start fresh" by setting currentSum
            #    to just the current array value
            currentSum = max(currentNum + currentSum, currentNum)

            # If this iteration of currentSum exceeds maxSum, update maxSum
            maxSum = max(currentSum, maxSum)

        return maxSum
