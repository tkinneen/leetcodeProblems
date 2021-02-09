class Solution:
	#def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
	def findMedianSortedArrays(self, nums1, nums2):

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