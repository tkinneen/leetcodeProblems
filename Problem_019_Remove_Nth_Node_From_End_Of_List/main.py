from Solution import ListNode, Solution

def main():
    
    # Create first node and set the head ptr
    testListHead = testList = ListNode(1)
    testList.next = ListNode(2)
    testList = testList.next
    testList.next = ListNode(3)
    testList = testList.next
    testList.next = ListNode(4)
    testList = testList.next
    testList.next = ListNode(5)
    nodeToRemove = 2

    #testListHead = testList = ListNode(1)
    #nodeToRemove = 1

    #testListHead = testList = ListNode(1)
    #testList.next = ListNode(2)
    #nodeToRemove = 1

    testList = testListHead

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.removeNthFromEnd(testList, nodeToRemove)

    print(f"Updated list with the node {nodeToRemove} from the end removed:")
    
    while answer:
        print(answer.val)
        answer = answer.next


if __name__ == "__main__":
	main()