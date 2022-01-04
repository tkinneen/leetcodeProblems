// 3. Longest Substring Without Repeating Characters 
// Given a string s, find the length of the longest substring without repeating characters.

#include <iostream>
#include <string>
#include <unordered_map>
#include "Solution.h"

int main() {
	
	Solution s;
	std::string testString = "abcabcbb";
	
	int answer = s.lengthOfLongestSubstring(testString);	

	std::cout << "main answer: " << answer << std::endl;
	
	return 0;

}
