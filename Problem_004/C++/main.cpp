// 4. Median of Two Sorted Arrays
// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// Follow up: The overall run time complexity should be O(log (m+n)).

#include <iostream>
#include <bits/stdc++.h>
//#include <string>
//#include <unordered_map>
//#include <sort>
#include <vector>
#include "Solution.h"

int main() {
	
	Solution s;

	std::vector<int> nums1 = {1, 3};
	std::vector<int> nums2 = {2};

	double answer = s.findMedianSortedArrays(nums1, nums2);	

	std::cout << "main answer: " << answer << std::endl;
	
	return 0;

}
