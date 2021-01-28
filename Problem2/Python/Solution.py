# Singly-linked list
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        # If either list contains a leading 0 or only has one node, return the other linked list
        if list1.val == 0 and list1.next == None:
            return list2
        if list2.val == 0 and list2.next == None:
            return list1
        
        list1FullNumber = ""
        list2FullNumber = ""
        
        # Loop through nodes and build the string of contained numbers
        while list1 or list2:
            if list1 != None:
                list1FullNumber = str(list1.val) + list1FullNumber           
                list1 = list1.next

            if list2 != None:
                list2FullNumber = str(list2.val) + list2FullNumber
                list2 = list2.next
        
        # Add the two full numbers, then cast result as string for easy breakdwon into linked list
        answer = str(int(list1FullNumber) + int(list2FullNumber))
    
        answerNode = ListNode(0)
        first = False # Flag to set the start pointer

        # Loop through the answer sum backwards and creat a linked list containing a node for each digit
        for x in reversed(answer):
            answerNode.next = ListNode(int(x))
            answerNode = answerNode.next

            # Set start pointer the first time through the loop
            if first == False:
                first = True
                start = answerNode

        answerNode = start # Reset linked list to beginning
        
        return answerNode
