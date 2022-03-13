from Solution import ListNode, Solution

def main():
	
    # Build the linked lists with the test inputs
    # Start pointer references the head, which we pass to solution
    listOneStart = listOne = ListNode(2)
    listOne.next = ListNode(4)
    listOne = listOne.next
    listOne.next = ListNode(3)
    listOne = listOneStart

    listTwoStart = listTwo = ListNode(5)
    listTwo.next = ListNode(6)
    listTwo = listTwo.next
    listTwo.next = ListNode(4)
    listTwo = listTwoStart

    # Instantiate Solution class
    s = Solution() 
                
    # Run the Solution method
    answer = s.addTwoNumbers(listOne, listTwo)

    # Loop through answer list and print all nodes
    while answer:
        print(str(answer.val))
        answer = answer.next


if __name__ == "__main__":
	main()