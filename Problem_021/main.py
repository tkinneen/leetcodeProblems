from Solution import Solution, ListNode

def main():
    
    # Build up both lists with the test values, node by node
    # testLists are pointers to the head, which we will pass in to the solution
    testList1 = buildList1 = ListNode(1)  # 1, 2, 4
    buildList1.next = ListNode(2)
    buildList1 = buildList1.next
    buildList1.next = ListNode(4)
    buildList1 = buildList1.next

    testList2 = buildList2 = ListNode(1) # 1, 3, 4
    buildList2.next = ListNode(3)
    buildList2 = buildList2.next
    buildList2.next = ListNode(4)
    buildList2 = buildList2.next

    # Instantiate Solution class
    s = Solution()

    # Run the Solution method on all test cases
    answer = s.mergeTwoLists(testList1, testList2)

    # Traverse the list and print each node's value
    while answer:
        print(answer.val)
        answer = answer.next


if __name__ == "__main__":
        main()