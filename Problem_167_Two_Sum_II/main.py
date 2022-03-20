from Solution import Solution

def main():

    testInput = [2,7,11,15]
    target = 9

    #testInput = [2,3,4]
    #target = 6

    #testInput = [-1,0]
    #target = -1

    # instantiate Solution class
    s = Solution() 

    answer = s.twoSum(testInput, target)

    print(answer)


if __name__ == "__main__":
	main()