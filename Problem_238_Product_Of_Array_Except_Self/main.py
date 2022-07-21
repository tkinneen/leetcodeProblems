from Solution import Solution


def main():

    testInput = [1, 2, 3, 4]  # Output: [24, 12, 8, 6]
    # testInput = [-1, 1, 0, -3, 3] # Output: [0, 0, 9, 0, 0]

    # instantiate Solution class
    solution = Solution()

    answer = solution.productExceptSelf(testInput)

    print(f"Products of each array element except self: {answer}")


if __name__ == "__main__":
    main()
