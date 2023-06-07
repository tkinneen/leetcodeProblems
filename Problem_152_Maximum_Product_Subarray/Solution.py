# LeetCode Problem 152: Maximum Product Subarray
#
# Given an integer array nums, find a subarray that has the largest product, and
#    return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Time complexity: O(n) - Entire array must be traversed
        # Memory complexity: O(1) - We're only tracking individual variables

        print(f"nums at the outset: {nums}")

        # Initialize the result to the largest number in the array
        result = max(nums)

        # Initialize to neutral 1's, they'll become whatever they're multiplied by
        curMin, curMax = 1, 1

        # 
        for curNum in nums:
            print(f"top of the loop: curMax: {curMax}, curMin: {curMin}, curNum: {curNum}")

            # This value is needed to calculate both currentMax and currentMin,
            #    and
            temp = curNum * curMax
            print(f"curNum ({curNum}) * curMax ({curMax}): {temp}")

            #
            print(f"taking max of (curNum * curMax) {curNum * curMax}, (curNum * curMin) {curNum * curMin}, and (curNum) {curNum}")
            print(f"taking min of (curNum * curMax) {temp}, (curNum * curMin) {curNum * curMin}, and (curNum) {curNum}")

            curMax = max(curNum * curMax, curNum * curMin, curNum)
            curMin = min(temp, curNum * curMin, curNum)

            print(f"curMax: {curMax}, curMin: {curMin}")

            # Update the result if currentMax exceeds it
            result = max(result, curMax)

            print(f"running result: {result}")
            print(f"========")

        print(f"final result: {result}")

        return result
