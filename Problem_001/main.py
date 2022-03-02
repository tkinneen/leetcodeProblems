from Solution import Solution

def main():

    #targetValue = 9
    #testInput = [2,7,11,15]
    
    #targetValue = 6
    #testInput = [3,2,4]

    targetValue = 6
    testInput = [3,3]

    # instantiate Solution class
    s = Solution() 

    answer = s.twoSum(testInput, targetValue)

    print(answer)


if __name__ == "__main__":
	main()