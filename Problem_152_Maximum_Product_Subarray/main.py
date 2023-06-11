from Solution import Solution

def main():

    testInput = [2,3,-2,4] # Output: 6
    #testInput = [-2,0,-1] # Output: 0
    testInput = [4,9,-2,0, -11, 12] # Output: 6
    #testInput = [2,3,-2,4] # Output: 6

    # Instantiate Solution class
    solution = Solution()

    result = solution.maxProduct(testInput)

    print(f"Maximum product subarray: {result}")


if __name__ == "__main__":
	main()