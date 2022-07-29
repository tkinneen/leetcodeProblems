# LeetCode Problem 056: Merge Intervals
#
# Given an array of intervals where intervals[i] = [starti, endi], merge
#    all overlapping intervals, and return an array of the non-overlapping
#    intervals that cover all the intervals in the input.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Time complexity is O(n log n) because we need to sort the array

        # Use lambda function to sort array of tuples by starting element
        intervals.sort(key=lambda i: i[0])

        # For each iteration, we will be comparing the current interval to the
        #    one that came before it
        result = [intervals[0]]
        print(f"original result: {result}")

        # Loop through sorted interval array, starting from first index position
        #    Extract the start and end points of current interval each iteration
        for start, end in intervals[1:]:

            # Extract the end value of the previous interval
            prevEnd = result[-1][1]

            # If the current start value is less or equal to the previous end,
            #    the intervals need to be merged. We do this by updating the
            #    end value of the most recent entry in the result array with
            #    the greater of the two end points being compared
            if start <= prevEnd:
                result[-1][1] = max(prevEnd, end)
            else:
                # If start value is greater than previous end, simply add
                #    current interval to result
                result.append([start, end])

        return result
