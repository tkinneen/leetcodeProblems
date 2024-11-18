from Solution import ListNode, Solution

def main():
    
    testLists = []

    # Create first node and set the head ptr
    listOneHead = listOne = ListNode(1)
    listOne.next = ListNode(4)
    listOne = listOne.next
    listOne.next = ListNode(5)
    listOne = listOne.next

    listTwoHead = listTwo = ListNode(1)
    listTwo.next = ListNode(3)
    listTwo = listTwo.next
    listTwo.next = ListNode(4)
    listTwo = listTwo.next

    listThreeHead = listThree = ListNode(2)
    listThree.next = ListNode(6)

    listFourHead = listFour = ListNode(11)
    listFour.next = ListNode(13)
    listFour = listFour.next
    listFour.next = ListNode(14)
    listFour = listFour.next

    listFiveHead = listFive = ListNode(21)
    listFive.next = ListNode(23)
    listFive = listFive.next
    listFive.next = ListNode(24)
    listFive = listFive.next

    testLists.append(listOneHead)
    testLists.append(listTwoHead)
    testLists.append(listThreeHead)
    testLists.append(listFourHead)
    testLists.append(listFiveHead)

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.mergeKLists(testLists)

    print("Merged linked list values: ")
    
    while answer:
        print(answer.val)
        answer = answer.next


if __name__ == "__main__":
	main()