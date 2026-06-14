from Solution import Solution

def main():

    # Output: [[0,0,0],[0,1,0],[0,0,0]]
    test_matrix = [[0,0,0],[0,1,0],[0,0,0]]

    # Output: [[0,0,0],[0,1,0],[1,2,1]]
    test_matrix = [[0,0,0],[0,1,0],[1,1,1]]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.updateMatrix(test_matrix)

    print(f"Result matrix: {result}")
    

if __name__ == "__main__":
	main()