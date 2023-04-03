from Solution import Solution

def main():
    
    testInput = [3,0,1] # Output: 2
    #testInput = [0,1] # Output: 2
    #testInput = [9,6,4,2,3,5,7,0,1] # Output: 8
    #testInput = [0,1,2] # Output: 3

    # Instantiate Solution class
    s = Solution()

    result = s.missingNumber(testInput)

    print(f"Missing number in the array: {result}")


if __name__ == "__main__":
	main()