from Solution import Solution

def main():

    # Example 1:
    n = 2 # Output: 1
    
    # Example 2:
    n = 3 # Output: 2
    
    # Example 3:
    n = 4 # Output: 3

    # Instantiate Solution class
    s = Solution() 

    # Retrieve solution
    answer = s.fib(n)

    print(f"Result: {answer}")


if __name__ == "__main__":
	main()