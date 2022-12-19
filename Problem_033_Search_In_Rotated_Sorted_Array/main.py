from Solution import Solution

def main():

    # Test Input 1
    #s = "anagram"
    #t = "nagaram"

    # Test Input 2
    s = "rat"
    t = "car"

    # instantiate Solution class
    solution = Solution()

    answer = solution.isAnagram(s, t)

    print("s is a valid anagram of t:")
    print(answer)


if __name__ == "__main__":
	main()