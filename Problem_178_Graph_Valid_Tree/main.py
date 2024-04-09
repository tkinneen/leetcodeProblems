from Solution import Solution

def main():

    # Example 1
    n = 5 
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # Output: True

    # Example 2
    #n = 5 
    #edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    # Output: False

    # instantiate Solution class
    solution = Solution()

    answer = solution.valid_tree(n, edges)

    print(f"Is the test input a valid tree?: {answer}")

if __name__ == "__main__":
    main()
