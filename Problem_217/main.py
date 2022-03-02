from Solution import Solution

def main():

    #testInputs = [1,2,3,1]
    #testInputs = [1,2,3,4]
    testInputs = [1,1,1,3,3,4,3,2,4,2]

    # instantiate Solution class
    s = Solution()

    answer = s.containsDuplicate(testInputs)

    print(answer)


if __name__ == "__main__":
	main()