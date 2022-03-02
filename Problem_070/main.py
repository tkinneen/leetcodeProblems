from Solution import Solution

def main():

    # testInputs 
    n = 22    
    # n = 3    
    # n = 5

    # instantiate Solution class
    s = Solution() 

    answer = s.climbStairs(n)

    print(answer)


if __name__ == "__main__":
	main()