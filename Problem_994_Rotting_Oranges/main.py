from Solution import Solution

def main():

    # Test case 1 - Output: 4
    test_grid = [[2,1,1],[1,1,0],[0,1,1]]

    # Test case 2 - Output: -1
    # test_grid = [[2,1,1],[0,1,1],[1,0,1]]

    # Test case 3 - Output: 0
    # test_grid = [[0,2]]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.orangesRotting(test_grid)

    if result == -1:
        print(f"Solution is impossible, fresh fruit remain in the grid.")
    else:
        print(f"Number of minutes before all oranges are rotten: {result}")
    

if __name__ == "__main__":
	main()