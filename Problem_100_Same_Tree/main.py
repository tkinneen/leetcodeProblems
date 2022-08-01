from Solution import Solution, TreeNode


def main():

    # Example 1
    # Create first list node and set the head pointer there
    treeNodeHead1 = testTree1 = TreeNode(1)
    testTree1.left = TreeNode(2)
    testTree1.right = TreeNode(3)
    testTree1 = testTree1.right
    testTree1.left = TreeNode(6)
    testTree1.right = TreeNode(7)

    treeNodeHead2 = testTree2 = TreeNode(1)
    testTree2.left = TreeNode(2)
    testTree2.right = TreeNode(3)

    # Example 2
    """treeNodeHead1 = testTree1 = TreeNode(1)
    testTree1.left = TreeNode(2)

    treeNodeHead2 = testTree2 = TreeNode(1)
    testTree2.right = TreeNode(2)"""

    # Example 3
    """treeNodeHead1 = testTree1 = TreeNode(1)
    testTree1.left = TreeNode(2)
    testTree1.right = TreeNode(1)

    treeNodeHead2 = testTree2 = TreeNode(1)
    testTree2.left = TreeNode(1)
    testTree2.right = TreeNode(2)"""

    # instantiate Solution class
    solution = Solution()

    answer = solution.isSameTree(treeNodeHead1, treeNodeHead2)

    print(f"The two trees are the same: {answer}")


if __name__ == "__main__":
    main()
