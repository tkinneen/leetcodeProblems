from Solution import Solution

def main():
    
    # Test Case 1 - Output: 6
    test_grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]

    # Test Case 2 - Output: 0
    # test_grid = [[0,0,0,0,0,0,0,0]]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.maxAreaOfIsland(test_grid)

    print(f"Maximum island area: {result}")
    

if __name__ == "__main__":
	main()