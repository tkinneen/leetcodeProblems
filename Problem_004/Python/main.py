# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).

from Solution import Solution

def main():
	
	testInput1 = [1, 3]
	testInput2 = [2]

	# instantiate Solution class
	s = Solution()

	# Solution returns an int length of the longest non-repeating substring in the testString
	answer = s.findMedianSortedArrays(testInput1, testInput2)

	print("answer in main: ")
	print(answer)

if __name__ == "__main__":
	main()
