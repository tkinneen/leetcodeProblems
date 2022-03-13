from Solution import Solution

def main():
    
    height = [1,8,6,2,5,4,8,3,7]
    #height = [1,1]

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.maxArea(height)

    print("The maximum amount of water the container can store is: " + str(answer))


if __name__ == "__main__":
	main()