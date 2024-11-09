from Solution import Solution

def main():

    testString = "abcabcbb" # Output: 3
    testString = "bbbbb" # Output: 1
    testString = "pwwkew" # Output: 3

    # instantiate Solution class
    s = Solution()

    # Solution returns an int length of the longest non-repeating substring in the testString
    answer = s.lengthOfLongestSubstring(testString)

    print(answer)


if __name__ == "__main__":
    main()