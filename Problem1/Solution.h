class Solution {
public:
    
	std::vector<int> twoSum(std::vector<int>& nums, int target) {
		// A brute force solution would require nested for loops (exponential time complexity)
		// The below solution is O(n) time complexity, achieved by using a hash map 
		
		std::vector<int> answer;
		std::unordered_map<int, int> valueMap;
		
		// Loop through all input elements, adding each to map
		for(auto i = 0; i < nums.size(); i++) {
		
			// find the complement to the current number that equals the target	
			int complement = target - nums[i];
			
			// If current value and complement add up to target, push each array element to answer vector 
			if(valueMap.find(complement) != valueMap.end()) {
				answer.push_back(valueMap[complement]);
				answer.push_back(i);
				return answer;
			}
			
       		valueMap[nums[i]] = i; 
		}
		// if no match is found still return vector
		return answer;
	}
};


