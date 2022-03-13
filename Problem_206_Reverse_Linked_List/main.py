from Solution import ListNode, Solution

def main():
    
    # Create first list node and set the head pointer there
    testListHead = testList = ListNode(1)
    
    # Populate the remaining nodes of the test list
    for i in range(2, 6):
        testList.next = ListNode(i)
        testList = testList.next
    
    # Set the pointer back to the beginning of the linked list
    testList = testListHead

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.reverseList(testList)

    # Traverse the list and print each value one by one
    print("Final answer")
    while answer:
        print(answer.val)
        answer = answer.next


if __name__ == "__main__":
	main()