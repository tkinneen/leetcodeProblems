# LeetCode Problem 338: Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each
#    i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
#   of i.

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        print(f"dp at the outset: {dp}")
        # result = [0]
        offset = 1

        for i in range(1, n + 1):
            print(f"i: {i}")

            if offset * 2 == i:
                offset = i
                print(f"offset getting updated to: {i}")

            print(f"dp[i - offset]: {dp[i - offset]}")

            dp[i] = 1 + dp[i - offset]
            print(f"dp: {dp}")
            print(f"=====================")

        return dp
