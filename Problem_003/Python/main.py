# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.  

from Solution import Solution

def main():
	
	testString = "abcabcbb"

	# instantiate Solution class
	s = Solution()

	# Solution returns an int length of the longest non-repeating substring in the testString
	answer = s.lengthOfLongestSubstring(testString)

if __name__ == "__main__":
	main()
