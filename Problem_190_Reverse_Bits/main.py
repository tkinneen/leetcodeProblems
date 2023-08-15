from Solution import Solution

def main():
    
    testInput = 0b00000010100101000001111010011100 # Output:    964176192 (00111001011110000010100101000000)
    testInput = 0b11111111111111111111111111111101 # Output:   3221225471 (10111111111111111111111111111111)
    testInput = 0b00000000000000000000000000001100 # Output:    964176192 (00111001011110000010100101000000)
    


    # Instantiate Solution class
    s = Solution()

    # Call the solution function
    result = s.reverseBits(testInput)

    print(f"Bits of test input {testInput}, reversed: {result}")


if __name__ == "__main__":
	main()