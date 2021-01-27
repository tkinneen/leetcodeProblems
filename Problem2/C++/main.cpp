// 2. Add Two Numbers 

// You are given two non-empty linked lists representing two non-negative integers. The digits 
//   are stored in reverse order, and each of their nodes contains a single digit. Add the two 
//   numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
