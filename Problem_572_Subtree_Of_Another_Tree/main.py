from Solution import Solution, TreeNode


def main():

    # Example 1 - Build the test tree and its potential subtree
    treeNode1Head = testTree1 = TreeNode(3)
    testTree1.left = TreeNode(4)
    testTree1.right = TreeNode(5)
    testTree1 = testTree1.left
    testTree1.left = TreeNode(1)
    testTree1.right = TreeNode(2)
    testTree1 = testTree1.right
    testTree1.left = TreeNode(0)

    treeNode2 = TreeNode(4)
    treeNode2.left = TreeNode(1)
    treeNode2.right = TreeNode(2)


    # Example 2 - Build the test tree and its potential subtree
    treeNode1Head = treeNode1 = TreeNode(3)
    treeNode1.left = TreeNode(4)
    treeNode1.right = TreeNode(5)
    treeNode1 = treeNode1.left
    treeNode1.left = TreeNode(1)
    treeNode1.right = TreeNode(2)

    treeNode2 = TreeNode(4)
    treeNode2.left = TreeNode(1)
    treeNode2.right = TreeNode(2)

    root, subroot = treeNode1Head, treeNode2

    # instantiate Solution class
    solution = Solution()

    answer = solution.isSubtree(root, subroot)

    print(f"Is subroot a subtree of root?: {answer}")


if __name__ == "__main__":
    main()
