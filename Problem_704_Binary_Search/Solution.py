# LeetCode Problem 704: Binary Search
#
# Given an array of integers nums which is sorted in ascending order, and an
#   integer target, write a function to search target in nums. If target
#   exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set pointers at each end of the array
        l, r = 0, len(nums) - 1

        # Loop until the pointers cross each other
        while l <= r:
            # Calculate the midpoint between the two pointers. // is
            #    division floor, so even-numbered arrays will err to
            #    the left of the two middle numbers
            m = (l + r) // 2

            # If not using Python, a very large input array could
            #    overflow the 32-bit integer max when adding the two
            #    index positions together to calculat midpoint
            # We can avoid this by subtracting the right index value
            #    from the left, then dividing by 2 will give half the
            #    distance betwen the positons. We can then ADD that
            #    to the current left ptr to get the midpoint, like so:
            # m = l + ((r - l) // 2)

            # If the midpoint is greater than the target, then the target
            #    resides in the left portion of the array. Throw away the
            #    entire right portion, INCLUDING the midpoint
            if nums[m] > target:
                r = m - 1

            # If the midpoint is less than the target, then the target
            #    resides in the right portion of the array. Throw away the
            #    entire left portion, INCLUDING the midpoint
            elif nums[m] < target:
                l = m + 1

            # The midpoint IS the target, we've found our answer
            else:
                return m

        return -1
