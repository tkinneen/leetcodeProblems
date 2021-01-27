// 1. Two Sum 
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

#include <iostream>
#include <vector>
#include <unordered_map>
#include "Solution.h"

int main() {
	
	Solution s;
	
	std::vector<int> testInputs = {2, 7, 11, 15};
	int targetValue = 9;
	
	s.twoSum(testInputs, targetValue);	
	
	return 0;

}
