from Solution import Solution, TreeNode

def main():
    # Build the binary tree that will be used as both example inputs
    treeNodeHead1 = testTree1 = TreeNode(6)
    testTree1.left = TreeNode(2)
    testTree1.right = TreeNode(8)
    testTree1 = testTree1.left
    testTree1.left = TreeNode(0)
    testTree1.right = TreeNode(4)
    testTree1 = testTree1.right
    testTree1.left = TreeNode(3)
    testTree1.right = TreeNode(5)
    testTree1 = treeNodeHead1
    testTree1 = testTree1.right
    testTree1.left = TreeNode(7)
    testTree1.right = TreeNode(9)
    testTree1 = treeNodeHead1

    # Example 1 - Output: 6
    p = TreeNode(2)
    q = TreeNode(8)

    # Example 2 - Output: 2
    #p = TreeNode(2)
    #q = TreeNode(4)

    # Example 3 - Output: 2
    # Build Tree specific to Example 3
    #testTree1 = TreeNode(2)
    #testTree1.left = TreeNode(1)
    #p = TreeNode(2)
    #q = TreeNode(1)

    # instantiate Solution class
    solution = Solution()

    answer = solution.lowestCommonAncestor(testTree1, p, q)

    print(f"Answer: {answer}")
    if answer:
        print(f"Lowest common ancestor of {p.val} and {q.val}: {answer.val}")

if __name__ == "__main__":
    main()