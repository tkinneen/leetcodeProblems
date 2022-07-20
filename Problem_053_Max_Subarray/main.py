from Solution import Solution


def main():

    testInput = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Output: 6
    # testInput = [1]  # Output: 1
    # testInput = [5, 4, -1, 7, 8]  # Output: 23

    # instantiate Solution class
    solution = Solution()

    answer = solution.maxSubArray(testInput)

    print(f"Sum of the maximum contiguous subarray: {answer}")


if __name__ == "__main__":
    main()
