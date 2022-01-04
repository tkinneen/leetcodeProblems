# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
	def twoSum(self, nums, target):

		# A brute force solution would use nested for loops (exponential time complexity)
		# The below solution is O(n) time complexity, achieved by using a dictionary (hash map) 
		
		answer = [] # Will contain index postions of numbers that add up to the target
		previousNumbers = {} # After each loop we add each iteration to the hash map for fast lookup

		for i, num in enumerate(nums):
		
			# Subtract the current number from the target number to find the complement value we need	
			complement = target - num 
		
			# If the current number's complement exists in the hash map, pack complement's index position and 
			# the current index postion in the answer array	
			if complement in hashMap:
				answer.append(hashMap[complement])
				answer.append(i)
				return answer
		
			# Add the current number to the has map if no answer has been found yet	
			hashMap[num] = i
			
		return answer
