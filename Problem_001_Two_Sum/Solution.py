# LeetCode Problem 001: Two Sum
# Given an array of integers nums and an integer target, return indices
#    of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and
#    you may not use the same element twice.
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute forcing would use nested for loops (exponential time complexity)
        # The below hash map solution is O(n) time complexity

        # After we see a number we add it to the hash map
        seenNums = {}

        for i, curNum in enumerate(nums):
            # Subtract the current number from the target number to find the complement value we need
            complement = target - curNum

            # If the current number's complement exists in the hash map, pack complement's index position and
            # the current index postion in the answer array
            if complement in seenNums:
                return [seenNums[complement], i]
            else:
                # Otherwise, add the current number and its index to the hashmap
                seenNums[curNum] = i

        # No answer was found
        return []
