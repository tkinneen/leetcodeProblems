from Solution import Solution

def main():

    # Instantiate Solution class
    s = Solution()

    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    #edges = [[0, 1], [2, 3], [4, 5]]
    #edges = []

    result = s.countComponents(n, edges)
    print(f"Number of connected components: {result}")
    

if __name__ == "__main__":
    main()
