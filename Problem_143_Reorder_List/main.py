from Solution import ListNode, Solution

def main():

    # Build up the test list - Output: [1,4,2,3]
    """testListHead = testList = ListNode(1)
    testList.next = ListNode(2)
    testList = testList.next
    testList.next = ListNode(3)
    testList = testList.next
    testList.next = ListNode(4)"""

    # Build up the test list - Output: [1,5,2,4,3]
    testListHead = testList = ListNode(1)
    testList.next = ListNode(2)
    testList = testList.next
    testList.next = ListNode(3)
    testList = testList.next
    testList.next = ListNode(4)
    testList = testList.next
    testList.next = ListNode(5)

    # Set ptr to head of list after building it
    testList = testListHead

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    s.reorderList(testList)

    print(f"Reordered list:")
    
    # Traverse the list, printing each value of its new order
    while testList:
        print(testList.val)
        testList = testList.next


if __name__ == "__main__":
	main()