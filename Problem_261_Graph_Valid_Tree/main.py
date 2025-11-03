from Solution import Solution

def main():
    
    #  Example 1 - Output: True
    n = 5 
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
 
    # Example 2 - Output: False
    #n = 5 
    #edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

    # Instantiate Solution class
    s = Solution()

    # Returns a single node of the cloned graph that is fully connected to all other nodes
    result = s.validTree(n, edges)

    print(f"Does the passed-in graph form a valid tree? {result}")

if __name__ == "__main__":
    main()
