from Solution import Solution

def main():

    # Output: 1
    testGrid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    # Output: 3
    testGrid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.numIslands(testGrid)

    print(f"Number of islands found: {result}")

if __name__ == "__main__":
	main()