from Solution import Solution


def main():
    nums = [-1, 0, 3, 5, 9, 12]  # Output: 4
    target = 9

    # nums = [-1,0,3,5,9,12] # Output: -1
    # target = 2

    # instantiate Solution class
    solution = Solution()

    result = solution.search(nums, target)

    print(f"Index position of the target: {result}")


if __name__ == "__main__":
    main()
