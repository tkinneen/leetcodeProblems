# LeetCode Problem 4: Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
#    return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).

from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

		# Becase, we always want nums1 to be the shorter array
		if len(nums1) > len(nums2):
			temp = nums1
			nums1 = nums2
			nums2 = temp
		
		low = 0
		high = len(nums1)
		combinedLength = len(nums1) + len(nums2)

		print(combinedLength)

		return 1.5