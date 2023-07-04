# LeetCode Problem 338: Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each
#    i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
#   of i.

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # Brute force complexity: O(n log n); Each iteration would require 
        #    a calculation of log n complexity (modulous 2 solution) 
        # Optimal solution uses dynamic programming, where the result of
        #    previous iterations are used to calculate the most recent iteration
        # Time complexity: O(n), Space complexity: O(n) since the  solution 
        #    requires an array of size (n+1)
        
        # Initialize an array containing the number of elements of the passed-in 
        #    value, plus the 0th position
        result = [0] * (n + 1)

        # This variable tracks when a new bit is required in our count. When 
        #    binary numbers count up from 0, the same pattern repeats itself over
        #    and over in the less significant bits. Knowing this, if we subtract 
        #    the offset from our current value, we can use the previous result at that 
        #    index position and add 1 to it (our new bit) to get the current result.
        #    In this way we essentially "count up" each time we get a new bit: 
        #    (4 + 0 = 4, 4 + 1 = 5, 4 + 2 = 6, 4 + 3 = 7, 8 + 0 = 8, 8 + 1 = 9, etc)
        offset = 1

        # Loop through each value in the passed in range. Start from 1 since 
        #    the 0th position was already initialized to 0 
        for curNum in range(1, n + 1):

            # This offset value will represent the most significant bit we've reached
            #    If the current number is twice the current offset, update it: we've 
            #    reached a new bit
            if offset * 2 == curNum:
                offset = curNum

            # Pack the current iteration's result into the result array 
            result[curNum] = 1 + result[curNum - offset]

        # The entire array has been populated, so return the result
        return result
