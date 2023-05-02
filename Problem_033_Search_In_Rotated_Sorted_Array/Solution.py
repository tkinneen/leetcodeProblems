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
        # Modified binary search solution: time complexity of O(log n)
        # When a problem specifies a log n solution, you should be thinking binary search

        # Set position pointers at far ends of the input array
        l, r = 0, len(nums) - 1

        # Loop until the left and right pointers meet
        # Needs to be less than or equal because we have to handle the condition of a single element
        while l <= r:
            # Calculate mid ptr each loop iteration
            # // is divison floor; evenly-numbered arrays will be left of mid
            mid = (l + r) // 2

            # When target matches the number at mid pointer, we have the answer
            if target == nums[mid]:
                return mid

            # Left portion - we know this is in sorted order, the pivot is elsewhere
            if nums[l] <= nums[mid]:
                # Check if the target exists in the bounds of this left portion. If so,
                #    shift the right ptr to left of mid. If not, shift left ptr to right
                #    of mid. Essentially discard the portion of the list with no target
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # Right portion - perform similar check as above
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        # If the pointers meet and that target hasn't been found, return -1
        return -1
