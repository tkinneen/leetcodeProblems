# LeetCode Problem 001: Two Sum
# Given an array of integers nums and an integer target, return indices
#    of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and
#    you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):

        # Brute forcing would use nested for loops (exponential time complexity)
        # The below hash map solution is O(n) time complexity
        
        # Contains index postions of numbers that add up to the target		
        answer = [] 

        # After we see a number we add it to the hash map
        previousNumbers = {} 

        for i, num in enumerate(nums):
		
            # Subtract the current number from the target number to find the complement value we need	
            complement = target - num 

            # If the current number's complement exists in the hash map, pack complement's index position and 
            # the current index postion in the answer array
            if complement in previousNumbers:
                answer.append(previousNumbers[complement])
                answer.append(i)
                return answer
		
            # Add the current number to the has map if no answer has been found yet
            previousNumbers[num] = i
			
        return answer