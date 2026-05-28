from Solution import Solution

def main():

    # Output: 4
    test_grid = [[2,1,1],[1,1,0],[0,1,1]]

    # Output: -1
    #test_grid = [[2,1,1],[0,1,1],[1,0,1]]

    # Output: 0
    #test_grid = [[0,2]]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.orangesRotting(test_grid)

    if result == -1:
          result = "Not Possible"

    print(f"Number of minutes to infect all oranges: {result}")

if __name__ == "__main__":
	main()