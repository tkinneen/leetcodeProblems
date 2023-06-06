from Solution import Solution


def main():
    testInput = 2  # Output: [0,1,1]
    testInput = 5  # Output: [0,1,1,2,1,2]
    testInput = 33  # Output: [0,1,1,2,1,2]
    testInput = 65  # Output: [0,1,1,2,1,2]

    # Instantiate Solution class
    s = Solution()

    result = s.countBits(testInput)

    print(f"Bit count array for input {testInput}: {result}")


if __name__ == "__main__":
    main()
