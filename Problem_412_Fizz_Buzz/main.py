from Solution import Solution


def main():

    # n = 3
    # n = 5
    n = 15

    # instantiate Solution class
    solution = Solution()

    answer = solution.fizzBuzz(n)

    print(f"Fizz Buzz results: {answer}")


if __name__ == "__main__":
    main()
