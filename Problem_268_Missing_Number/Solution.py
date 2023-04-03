# LeetCode Problem 268: Missing Number
#
# Given an array nums containing n distinct numbers in the range [0, n], return 
#    the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space complexity 
#    and O(n) runtime complexity?

from typing import List

class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:

        # Time complexity is O(n), as we loop once though every element in the array
        # Memory complexity is O(1) as we don't use any extra data structures

        # Two solutions are provided: An addition-subtraction solution, and an Xor solution.
        #    Both work similarly.

        # For addition-subtraction, we sum each value in the provided range, then sum 
        #    each value in the input array seprately. Then by subtracting the input array 
        #    sum from the range sum, we get the missing number

        # For the Xor solution, we perform a binary Xor on each number in the range with its
        #    adjacent number. Then we do the same for each element in the input array. By performing
        #    an Xor on the two resulting vlaues, we get the missing number

        # Both solutions will combine the two initial for loops into one single loop to save time.
        
        # Solution 1
        def missingNumberSubtraction(nums: List[int]) -> int:
            
            # Initialize the running result with the length of the number array. Since we are
            #    looping through the contents of the test input array (which is missing one
            #    number), we would otherwiese not have this value
            result = len(nums)

            for i in range(len(nums)):

                # For each iteration, subtract the current test input value from the current range value, 
                #    then add it to the running result. This would have the same effect as summing the 
                #    two arrays separately and subtracting the results
                result += (i - nums[i])

            return result

        # Solution 2
        def missingNumberBinaryXOR(nums: List[int]) -> int:
            
            # Initialize the running result for the same reason as above
            result = len(nums)
            
            for i in range(len(nums)):
                
                # For each iteration, Xor the current test input value with the current range value, 
                #    then Xor THAT value with the running result. This would have the same effect as 
                #    Xor'ing the two arrays separately and then again Xor'ing the results
                result ^= i ^ nums[i]

            return result
        

        finalResult = missingNumberSubtraction(nums)
        #finalResult = missingNumberBinaryXOR(nums)

        return finalResult