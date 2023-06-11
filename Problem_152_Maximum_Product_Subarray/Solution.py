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
        # Memory complexity: O(1) - Just tracking individual variables, ragardless of input size

        # Initialize result to first array input (as a starting point)
        result = nums[0]

        # Calculate the current min/max at each positon in the array
        #    Initialize to 1 as a neutral value that will take on any other value
        curMin, curMax = 1, 1

        # Because of the sign-flipping properties of negative multiplication, 
        #    we need to track the min/max values at each position of the array.
        #    Even though we only loop once, by tracking both we can test both 
        #    outcomes (current num times max if they're both positive, current num
        #    times min if they're both negative, or current num alone if both previous
        #    calculations result in a negative number
        # One thing to note is we don't care what subarray combination actually
        #    achieves the max product, we ONLY care about the max value
        for curNum in nums:

            # curMax is needed to calculate both the min and max for this iteration.
            #    Since calculating curMax will overwrite the previous value, cache 
            #    it for the current min calculation 
            cachedCurMax = curMax

            # Both min and max calculations use the same inputs
            curMax = max(curNum * curMax, curNum * curMin, curNum)
            curMin = min(curNum * cachedCurMax, curNum * curMin, curNum)

            # Check if the curMax exceeds our total max up to that point, and if so update value
            result = max(result, curMax)

        # When the loop exits, return the total max achieved
        return result