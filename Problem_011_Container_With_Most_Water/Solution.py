# LeetCode Problem 011: Container With Most Water
# You are given an integer array height of length n. There are n vertical
#    lines drawn such that the two endpoints of the ith line are (i, 0) and 
#    (i, height[i]).
# Find two lines that together with the x-axis form a container, such that 
#    the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Time complexity: O(n) - Memory complexity: O(1) 

        # Two pointer solution - start with one at each end of the height array
        leftPtr, rightPtr = 0, (len(height) - 1)
        maxArea = 0

        # Loop until the pointers meet
        while leftPtr < rightPtr:
            
            # Caluclate the area of the two heights:
            # The distance between the two pointers, multiplied by the LOWEST of the two 
            #    heights (as water would trickle over the top of the lower wall)
            currentArea = (rightPtr - leftPtr) * min(height[leftPtr], height[rightPtr])

            # Update the maximum area if the current exceeds it
            if currentArea > maxArea:
                maxArea = currentArea            
            
            # Each iteration move the pointer of lesser height towards its counterpart
            if height[rightPtr] < height[leftPtr]:
                rightPtr -= 1
            else:
                leftPtr += 1

        # Return max area calculated through all loops
        return maxArea
