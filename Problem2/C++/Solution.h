// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        // Carry value used when node additions exceed a single digit
        int carry = 0;
        
        // Create initial node and set head pointer
        ListNode *answerList = new ListNode(0);
        ListNode *answerHead = answerList;

        // Loop through both linked lists, adding values of each corresponding node
        while(l1 != NULL || l2 != NULL || carry > 0) {

            // Add carry of previous sum to current sum
            int currentSum = carry;
            
            // If the current node exists, add the value to the current sum
            if(l1 == NULL)
                currentSum += 0;
            else
                currentSum += l1->val;

            if(l2 == NULL)
                currentSum += 0;
            else
                currentSum += l2->val;
            
            // Each node value can only hold a single digit, so if the sum exceeds 9
            //     subtract 10 from the value and increment the carry for the next iteration
            if(currentSum > 9) {
                currentSum -= 10;
                carry = 1;
            } else
                carry = 0;

            // Create a new node with the current sum as the val, then navigate to it
            answerList->next = new ListNode(currentSum);
            answerList = answerList->next;

            // Move to the next node of each list if there is one
            if(l1 == NULL && l2 == NULL)
                break;
            else if(l1 == NULL)
                l2 = l2->next;
            else if(l2 == NULL)
                l1 = l1->next;
            else {
                l1 = l1->next;
                l2 = l2->next;
            }
        }
        
        // Reset answer list to the start pointer, then return
        answerList = answerHead->next;
        return answerList;
    }
};