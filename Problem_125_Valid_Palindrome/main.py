from Solution import Solution

def main():
    
    # Example 1:
    testString = "A man, a plan, a canal: Panama" # Output: true
    
    # Example 2:
    #testString = "race a car" # Output: false
    
    # Example 3:
    #testString = " " # Output: true
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.isPalindrome(testString)
    print(f"\n{testString} is a valid palindrome: {result}")


if __name__ == "__main__":
	main()
