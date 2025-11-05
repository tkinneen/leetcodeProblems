from Solution import Solution

def main():
    #  Example 1
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    # Example 2
    # heights = [[1]]
    # Output: [[0,0]]

    # Instantiate Solution class
    s = Solution()

    # Returns a single node of the cloned graph that is fully connected to all other nodes
    result = s.pacificAtlantic(heights)

    print(f"The following cells can flow to both the Pacific and Atlantic oceans: {result}")

if __name__ == "__main__":
    main()