// 1. Two Sum 
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

#include <iostream>
#include <vector>
#include <unordered_map>
#include "Solution.h"

int main() {
	
	Solution s;
	
	std::vector<int> testInputs = {2, 7, 11, 15};
	int target = 9;
	
	s.twoSum(testInputs, target);	
	
	return 0;

}
