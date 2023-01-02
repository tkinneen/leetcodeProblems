from Solution import Solution

def main():
    
    testInput = 0b00000000000000000000000000001011 # Output: 3
    #testInput = 0b00000000000000000000000010000000 # Output: 1
    #testInput = 0b11111111111111111111111111111101 # Output: 31

    # Instantiate Solution class
    s = Solution()

    # Two different solution functions
    result = s.hammingWeightModulus(testInput)
    #result = s.hammingWeightLogicalAnd(testInput)

    print(f"Number of 1 bits: {result}")


if __name__ == "__main__":
	main()