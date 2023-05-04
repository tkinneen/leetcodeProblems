from Solution import Solution


def main():
    a, b = 1, 2  # Output: 3
    # a, b = 2, 3 # Output: 5
    # a, b = -10, 2  # Output: 3
    # a, b = 14, 6  # Output: 3
    # a, b = 11, 101  # Output: 3
    # a, b = 202, 303  # Output: 3
    # a, b = 2000, 3000  # Output: 3

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.getSum(a, b)

    print(f"Sum of {a} and {b} (without using +/- operators): {result}")


if __name__ == "__main__":
    main()
