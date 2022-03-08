from Solution import Solution

def main():

    #testInput = "()"
    testInput = "()[]{}"
    #testInput = "([)]"

    # instantiate Solution class
    s = Solution()

    answer = s.isValid(testInput)

    print("String contains valid parenthesis: ")
    print(answer)


if __name__ == "__main__":
	main()