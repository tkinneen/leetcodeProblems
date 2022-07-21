# LeetCode Problem 238: Product of Array Except Self
#
# Given an integer array nums, return an array answer such that answer[i] is
#    equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a
#    32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the
#    division operation.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Time and space complexity are O(n)

        forwardArray = []
        backwardArray = []
        answerArray = []

        # Loop from the beginning to the end of the input array, multiplying each
        #    element by the running product
        currentProduct = 1
        for i in nums:
            currentProduct *= i
            forwardArray.append(currentProduct)

        # Reinitialize, then do the exact same thing in reverse for the backwardArray
        currentProduct = 1
        for i in reversed(nums):
            currentProduct *= i
            backwardArray.insert(0, currentProduct)

        # We will use these pre-multiplied arrays to calculate the answer from each
        #   index position, then pack each into the answer array

        # Loop through each element in the input array once more, multiplying
        #    the previous index position of the forward array with the next
        #    index position of the backward array. If going backwards or forwards
        #    of the current index exceeds the array bounds, just multiply by 1
        for i in range(len(nums)):
            if i == 0:
                answerArray.append(1 * backwardArray[i + 1])
            elif i == (len(nums) - 1):
                answerArray.append(forwardArray[i - 1] * 1)
            else:
                answerArray.append(forwardArray[i - 1] * backwardArray[i + 1])

        return answerArray
