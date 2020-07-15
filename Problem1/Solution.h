class Solution {
public:
    
	std::vector<int> twoSum(std::vector<int>& nums, int target) {
		// A brute force solution would require nested for loops (exponential time complexity)
		// The below solution is O(n) time complexity, and is achieved using a hash map 
		
		std::vector<int> answer;
		std::unordered_map<int, int> valueMap;
		
		// Loop through all input elements, add to hash map
		for(auto i = 0; i < nums.size(); i++) {
		
			// find the complement to the current number equalling the target	
			int complement = target - nums[i];

			if(valueMap.find(complement) != valueMap.end()) {
				answer.push_back(valueMap[complement]);
				answer.push_back(i);
				return answer;
			}
			
       		valueMap[nums[i]] = i; 
		}
	}
};


