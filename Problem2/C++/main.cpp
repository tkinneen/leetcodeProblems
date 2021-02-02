// 2. Add Two Numbers 

// You are given two non-empty linked lists representing two non-negative integers. The digits 
//     are stored in reverse order, and each of their nodes contains a single digit. Add the two 
//     numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#include <iostream>
#include <string>
#include "Solution.h"

int main() {
	
	// Instantiate Solution class
	Solution s;
	
	// Build the two linked lists with the test values
	ListNode* l1 = new ListNode(2);

	ListNode* l1_beginning = l1;
	l1->next = new ListNode(4);
	l1 = l1->next;
	l1->next = new ListNode(3);
	l1 = l1->next;
	l1 = l1_beginning; // Reset the list back to the start node

	ListNode* l2 = new ListNode(5);
	ListNode* l2_beginning = l2;
	l2->next = new ListNode(6);
	l2 = l2->next;
	l2->next = new ListNode(4);
	l2 = l2->next;
	l2 = l2_beginning;

	// Call the solution method and receive the answer linked list
	ListNode* answer = s.addTwoNumbers(l1, l2);
	
	return 0;

}
