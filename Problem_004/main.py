from Solution import Solution

def main():
	
	testInput1 = [1, 3]
	testInput2 = [2]

	# instantiate Solution class
	s = Solution()

	# Solution returns an int length of the longest non-repeating substring in the testString
	answer = s.findMedianSortedArrays(testInput1, testInput2)

	print(answer)


if __name__ == "__main__":
	main()