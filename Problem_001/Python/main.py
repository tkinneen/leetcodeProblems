from Solution import Solution

def main():

    testInputs = [2,7,11,15]
    targetValue = 9

    # instantiate Solution class
    s = Solution() 

    answer = s.twoSum(testInputs, targetValue)

    print(answer)


if __name__ == "__main__":
	main()