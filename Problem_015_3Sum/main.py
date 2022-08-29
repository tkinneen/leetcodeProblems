from Solution import Solution


def main():

    testInput = [-1, 0, 1, 2, -1, -4]

    -4 - 1 - 1 0 1 2
    # Output: [[-1, -1, 2], [-1, 0, 1]]

    #testInput = [0, 1, 1]
    # Output: []

    #testInput = [0, 0, 0]
    # Output: [[0, 0, 0]]

    # instantiate Solution class
    s = Solution()

    answer = s.threeSum(testInput)

    print(f"{answer}")


if __name__ == "__main__":
    main()
