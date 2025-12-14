from Solution import Solution

def main():

    # Test input - Number of stairs to calculate  
    # n = 3 # Output: 3
    # n = 4 # Output: 4
    # n = 5 # Output: 8
    n = 8 # Output: 34

    # Instantiate Solution class
    s = Solution() 

    # Retrieve solution
    answer = s.climbStairs(n)

    print(f"For an input of {n}, there are {answer} ways to climb to the top.")

if __name__ == "__main__":
	main()