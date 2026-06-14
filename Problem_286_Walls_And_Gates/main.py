from Solution import Solution

def main():

    # Example 1 - Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    test_grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]

    # Example 2 - Output: [[0,-1],[1,2]]
    #test_grid = [
    #    [0,-1],
    #    [2147483647,2147483647]
    #]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.wallsAndGates(test_grid)

    print(f"Result grid:")

    for row in result:
          print(row)

if __name__ == "__main__":
	main()