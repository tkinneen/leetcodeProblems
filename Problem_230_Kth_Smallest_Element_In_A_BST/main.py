from Solution import Solution, TreeNode

def main():
    # Build the binary tree that will be used as both example inputs
    treeNodeHead1 = testTree1 = TreeNode(3)
    testTree1.left = TreeNode(1)
    testTree1.right = TreeNode(4)
    testTree1 = testTree1.left
    testTree1.right = TreeNode(2)
    testTree1 = treeNodeHead1

    k = 1


    # Build the binary tree that will be used as both example inputs
    treeNodeHead1 = testTree1 = TreeNode(5)
    testTree1.left = TreeNode(3)
    testTree1.right = TreeNode(6)
    testTree1 = testTree1.left
    testTree1.left = TreeNode(2)
    testTree1.right = TreeNode(4)
    testTree1 = testTree1.left
    testTree1.left = TreeNode(1)
    testTree1 = treeNodeHead1

    k = 3

    solution = Solution()

    answer = solution.kthSmallest(testTree1, k)

    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()