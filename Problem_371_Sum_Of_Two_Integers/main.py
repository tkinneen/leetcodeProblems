from Solution import Solution

def main():
    a, b = 1, 2  # Output: 3
    #a, b = 2, 3 # Output: 5
    #a, b = 0, 1 # Output: 1
    #a, b = 1, 1 # Output: 2
    #a, b = -1, 1 # Output: 0
    #a, b = -2, 1 # Output: -1
    #a, b = -10, 1 # Output: -9

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.getSum(a, b)

    print(f"Sum of {a} and {b} (without using +/- operators): {result}")


if __name__ == "__main__":
    main()
