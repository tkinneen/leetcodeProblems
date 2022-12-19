from Solution import Solution

def main():

    testStrings = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    #testStrings = [""]
    # Output: [[""]]

    #testStrings = ["a"]
    # Output: [["a"]]

    # instantiate Solution class
    solution = Solution()

    answer = solution.groupAnagrams(testStrings)

    print(f"Grouped anagrams: {answer}")


if __name__ == "__main__":
	main()