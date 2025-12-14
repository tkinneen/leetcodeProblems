from Solution import Solution

def main():

    # Example 1:
    nums = [1,2,3,1] # Output: 4

    # Example 2:
    nums = [2,7,9,3,1] # Output: 12

    # Instantiate Solution class
    s = Solution() 

    # Retrieve solution
    answer = s.rob(nums)

    print(f"Maximum profit from robberies: {answer}")


if __name__ == "__main__":
	main()