from Solution import Solution


def main():

    testInput = [6, 7, 0, 1, 2, 4, 5]  # Output: 4
    target = 0
    #testInput = [0, 1, 2, 4, 5, 6, 7]  # Output: 4
    #target = 0
    #testInput = [4, 5, 6, 7, 0, 1, 2]  # Output: 4
    #target = 0
    # testInput = [4, 5, 6, 7, 0, 1, 2]  # Output: -1
    #target = 3
    # testInput = [1]  # Output: -1
    #target = 0

    # instantiate Solution class
    solution = Solution()

    answer = solution.search(testInput, target)

    print(f"Index position of target: {answer}")


if __name__ == "__main__":
    main()
