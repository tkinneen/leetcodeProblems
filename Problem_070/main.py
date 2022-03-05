from Solution import Solution

def main():

    # Test input - Number of stairs to calculate  
    # n = 3
    # n = 4   
    # n = 5
    n = 8

    # Instantiate Solution class
    s = Solution() 

    # Retrieve solution
    answer = s.climbStairs(n)

    print(answer)


if __name__ == "__main__":
	main()