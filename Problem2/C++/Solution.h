class Solution {
public:
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode * l1_check = l1;
        ListNode * l2_check = l2;
        
        int l1_count = 0;
        int l2_count = 0;
        
        while(l1_check != NULL) {
            l1_count++;
            l1_check = l1_check->next;
        }

        while(l2_check != NULL) {
            l2_count++;
            l2_check = l2_check->next;
        }
        
        if(l1_count != l2_count) {
            if(l1_count > l2_count)
                return l1;
            else
                return l2;
        }

        std::string num1 = "";
        std::string num2 = "";

        while(l1 != NULL) {
            
            num1 = num1 + std::to_string(l1->val);
            l1 = l1->next;
            l2 = l2->next;
            
            /*if(l1 == NULL && l2 != NULL)
                return l2;
            if(l1 != NULL && l2 == NULL)
                return l1;*/
            if(l2 != NULL) {
                num2 = num2 + std::to_string(l2->val);
                l2 = l2->next;
            }
        }
        
        int n1 = std::stoi(num1);
        int n2 = std::stoi(num2);
        
        std::cout << ("n1: ") << n1 << endl;
        std::cout << ("n2: ") << n2 << endl;

                
        int answer = n1 + n2;
        std::string strAnswer = std::to_string(answer);
        
        std::cout << ("strAnswer: ") << strAnswer << endl;
        

        ListNode * l3 = new ListNode(1);
        ListNode * l3_start = l3;
        std::cout << ("new listnode: ") << endl;
        std::cout << ("l3->val: ") << l3->val << endl;
        std::cout << ("l3->next: ") << l3->next << endl;

        for(auto it = (strAnswer.end() - 1) ; it >= strAnswer.begin(); it--) {
            std::cout << "*it" << endl;
            std::cout << *it << endl;
            
            int currentNumber = (*it - 48);
            
            std::cout << ("currentNumber: ") << currentNumber << endl;
            ListNode *temp = new ListNode(currentNumber);
            l3->next = temp;
            l3 = l3->next;               
            std::cout << (l3->val) << endl;
            
            std::cout << ("l3->val: ") << l3->val << endl;
        }
        
        l3 = l3_start;
        l3 = l3->next;
        return l3;
    }
};    
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


