from Solution import Solution

def main():

    testInput = [3,4,5,1,2] # Output: 1
    testInput = [4,5,6,7,0,1,2] # Output: 0
    #testInput = [11,13,15,17] # Output: 11
    
    # instantiate Solution class
    solution = Solution()

    result = solution.findMin(testInput)

    print(f"Minimum number in rotated, sorted array: {result}")


if __name__ == "__main__":
	main()