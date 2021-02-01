# Singly-linked list
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:

        # Carry value used when node additions exceed a single digit
        carry = 0
        
        # Create initial node and set head pointer
        answerHead = answerList = ListNode(0)

        # Loop through linked lists and sum values of each corresponding node
        while list1 or list2 or carry:
            
            # Add carry of previous sum to current sum
            currentSum = carry
            
            # If the current node exists, add the value to the current sum
            if list1 is None:
                currentSum += 0
            else:
                currentSum += list1.val

            if list2 is None:
                currentSum += 0
            else:
                currentSum += list2.val
            
            # Each node value can only hold a single digit, so if the sum exceeds 9
            #     subtract 10 from the value and increment the carry for the next iteration
            if currentSum > 9:
                currentSum -= 10
                carry = 1
            else:
                carry = 0

            # Create a new node with the current sum as the val, then navigate to it
            answerList.next = ListNode(currentSum)
            answerList = answerList.next

            # Move to the next node of each list if there is one
            if list1 is None and list2 is None:
                break
            elif list1 is None:
                list2 = list2.next
            elif list2 is None:
                list1 = list1.next
            else:
                list1 = list1.next
                list2 = list2.next

        # Reset answer list to the start pointer, then return
        answerList = answerHead.next
        return answerList
