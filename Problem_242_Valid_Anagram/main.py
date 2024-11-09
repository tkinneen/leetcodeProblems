from Solution import Solution

def main():

    # Test Input 1
    s = "anagram"
    t = "nagaram"

    # Test Input 2
    #s = "rat"
    #t = "car"

    # instantiate Solution class
    solution = Solution()

    answer = solution.isAnagram(s, t)

    if(answer):
        print(f"{s} is a valid anagram of {t}:")
    else:
        print(f"{s} is NOT a valid anagram of {t}:")

if __name__ == "__main__":
	main()