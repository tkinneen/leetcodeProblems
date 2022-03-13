from Solution import ListNode, Solution

def main():
    
    # Create first node and set the head ptr
    testListHead = testList = ListNode(3)

    # Add the second node and set a ptr that the end of the list can loop back to
    testList.next = ListNode(2)
    testList = testList.next
    loopback = testList

    # Populate the remaining nodes in the linked list
    testList.next = ListNode(0)
    testList = testList.next
    testList.next = ListNode(-4)
    testList = testList.next
    testList.next = loopback
    
    # Set ptr to beginning of list to pass to Solution class
    testList = testListHead

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.hasCycle(testList)

    print("The linked list contains a cycle: ")
    print(answer)


if __name__ == "__main__":
	main()