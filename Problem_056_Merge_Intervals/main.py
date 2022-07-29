from Solution import Solution


def main():

    # Output: [[1, 6], [8, 10], [15, 18]]
    testInput = [[1, 3], [8, 10], [2, 6], [15, 18]]
    # testInput = [[1, 4], [4, 5]] # Output: [[1, 5]]

    print(f"testInput: {testInput}")

    # instantiate Solution class
    solution = Solution()

    answer = solution.merge(testInput)

    print(f"Answer array of all merged, non-overlapping intervals: {answer}")


if __name__ == "__main__":
    main()
