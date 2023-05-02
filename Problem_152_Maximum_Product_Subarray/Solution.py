# LeetCode Problem 152: Maximum Product Subarray
#
# Given an integer array nums, find a subarray that has the largest product, and 
#    return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        print(f"nums: {nums}")

        # Initially set the original result to the largest number in the array
        result = max(nums)

        # 
        currentMin, currentMax = 1, 1

        for currentNum in nums:
            
            # Aparently not necessary
            #if currentNum == 0:
            #    currentMin, currentMax = 1, 1
            #    continue
            
            # Store this value; we need it to calculate both currentMax and currentMin, 
            #    and it will change after we calculate currentMax
            temp = currentNum * currentMax

            # 
            currentMax = max(currentNum * currentMax, currentNum * currentMin, currentNum)
            currentMin = min(temp, currentNum * currentMin, currentNum)

            print(f"currentMax: {currentMax}")
            print(f"currentMin: {currentMin}")


            # As necessary update the result if the currentMax is greater
            result = max(result, currentMax)

            print(f"result: {result}")
            print(f"========")

        
        return result
