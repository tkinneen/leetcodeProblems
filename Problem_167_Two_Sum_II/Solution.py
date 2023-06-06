# LeetCode Problem 167: Two Sum II
# Given a 1-indexed array of integers numbers that is already sorted in
#    non-decreasing order, find two numbers such that they add up to a
#    specific target number. Let these two numbers be numbers[index1] and
#    numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as
#    an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may
#    not use the same element twice.

# Your solution must use only constant extra space.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> int:
        # As we know the array is sorted, we can use a 2 pointer solution
        leftPtr = 0
        rightPtr = len(nums) - 1

        # Loop until the two pointers meet
        while leftPtr < rightPtr:
            # Sum the two values at the L and R ptr array positions
            twoSum = nums[leftPtr] + nums[rightPtr]

            # If current val overshoots the target, we move the R ptr one position
            #    to the left, as we know it will be smaller than the current R ptr
            if twoSum > target:
                rightPtr -= 1
            # If the current val undershoots, we move the L ptr to the right
            elif twoSum < target:
                leftPtr += 1
            # If current hits our target, return the L and R ptr postions.
            # This question considers first element in the array as 1 for some reason,
            #    so we bump both ptr positions by 1
            elif twoSum == target:
                return [leftPtr + 1, rightPtr + 1]

        # The question guarantees exactly one solution, so we never get here
        return []
