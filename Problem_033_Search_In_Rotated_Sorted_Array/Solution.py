# LeetCode Problem 033: Search In Rotated Sorted Array
# There is an integer array nums sorted in ascending order(with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown
#    pivot index k(1 <= k < nums.length) such that the resulting array is [nums[k],
#    nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]](0-indexed). For
#    example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3 and become
#    [4, 5, 6, 7, 0, 1, 2].
#
# Given the array nums after the possible rotation and an integer target, return the
#    index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # This is a binary search solution with a time complexity of O(log n)
        # When a problem specifies a log n solution, you should be thinking binary search

        # Set position pointers at opposite ends of the input array
        l, r = 0, len(nums) - 1
        print(f"length of input array: {len(nums) - 1}")

        # Loop until the left and right pointers meet
        while l <= r:

            # Calculate pointer at the midpoint of the array
            # // is divison floor, so mid in arrays with an even number of elements
            #    will err on the left side
            mid = (l + r) // 2
            print(f"mid: {mid}")

            # If the target matches the number at the mid pointer, we've found our
            #    answer, so return
            if target == nums[mid]:
                return mid

            # Left sorted portion
            if nums[l] <= nums[mid]:
                #
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # target > nums[mid] or target < nums[l]
                else:
                    r = mid - 1

            # Right sorted porition
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        # If the pointers meet and that target hasn't been found, return -1
        return -1
