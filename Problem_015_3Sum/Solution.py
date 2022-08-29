# LeetCode Problem 015: 3Sum
#
# Given an integer array nums, return all the triplets[nums[i], nums[j],
#    nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j]
#    + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Time complexity of O(n**2)
        # Depending on the efficiency of the sorting algorithm, space complexity is either O(1) or O(n)

        # Initialize result array - contains arrays of all permutations of values summing to 0
        result = []

        # Sort allows efficient duplicate checking
        nums.sort()

        # Outter loop steps through each value, and then the inner loop will use the same two-
        #    pointer solution as Two Sum II to find the complementary values
        for i, a in enumerate(nums):

            # Duplicates aren't allowed in the solution. Since we sorted the array we can
            #    move to the next value if it's the same as the previous
            if i > 0 and a == nums[i - 1]:
                continue

            # Set pointers for inner loop
            l, r = i + 1, len(nums) - 1

            # Walk pointers
            while l < r:
                # Calculate sum of 3 current values
                threeSum = a + nums[l] + nums[r]

                # Decrement right pointer if current value overshoots
                if threeSum > 0:
                    r -= 1
                # Increment left pointer if current value undershoots
                elif threeSum < 0:
                    l += 1
                # Just because we have a match doesn't mean there aren't more in this iteration
                else:
                    # Append the answer to the results array
                    result.append([a, nums[l], nums[r]])
                    # Continue incrementing pointer
                    l += 1
                    # Still perform duplicate check, increment pointer if it is
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result
