from Solution import Solution
def main():
    
    # Example 1, Output: true
    numCourses = 2
    prerequisites = [[1,0]]

    # Example 2, Output: false
    #numCourses = 2
    #prerequisites = [[1,0],[0,1]]

    # Instantiate Solution class
    s = Solution()

    # Returns 
    result = s.canFinish(numCourses, prerequisites)

    print(f"Can the courses be completed with the specified prerequisites? {result}")

if __name__ == "__main__":
    main()
