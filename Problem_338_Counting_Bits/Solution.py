# LeetCode Problem 338: Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each
#    i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
#   of i.

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Pad the array from 0 through the passed-in input
        result = [0] * (n + 1)
        print(f"dp at the outset: {result}")

        #
        offset = 1

        # Loop
        # Start at 1 because we padded entire array w/ 0's and 0 is 0
        for i in range(1, n + 1):
            print(f"i: {i}")

            if offset * 2 == i:
                offset = i
                print(f"offset getting updated to: {i}")

            print(f"result[i - offset]: {result[i - offset]}")
            print(f"offset: {offset}")
            print(f"i - offset: {i - offset}")

            result[i] = 1 + result[i - offset]
            print(f"result: {result}")
            print(f"=====================")

        return result
