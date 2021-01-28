# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The 
#     digits are stored in reverse order, and each of their nodes contains a single
#     digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from Solution import ListNode
from Solution import Solution

def main():
	
	# Build the linked lists with the test inputs
	listOne = ListNode(2)
	listOneStart = listOne
	listOne.next = ListNode(4)
	listOne = listOne.next
	listOne.next = ListNode(3)
	listOne = listOneStart # Reset the list to beginning

	listTwo = ListNode(5)
	listTwoStart = listTwo
	listTwo.next = ListNode(6)
	listTwo = listTwo.next
	listTwo.next = ListNode(4)
	listTwo = listTwoStart

	# instantiate Solution class
	s = Solution() 

	answer = s.addTwoNumbers(listOne, listTwo)
	
	print(answer.val)
	answer = answer.next
	print(answer.val)
	answer = answer.next
	print(answer.val)

if __name__ == "__main__":
	main()