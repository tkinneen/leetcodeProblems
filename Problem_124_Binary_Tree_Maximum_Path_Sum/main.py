from Solution import TreeNode, Solution

def main():
    
    # Build test tree - Example 1
    treeNodeHead = testTree = TreeNode(1)
    testTree.left = TreeNode(2)
    testTree.right = TreeNode(3)

    # Build test tree - Example 2
    treeNodeHead = testTree = TreeNode(-10)
    testTree.left = TreeNode(9)
    testTree.right = TreeNode(20)
    testTree = testTree.right
    testTree.left = TreeNode(15)
    testTree.right = TreeNode(7)

    # Point to the head before passing to the Solution class
    testTree = treeNodeHead
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.maxPathSum(testTree)
    print(f"Maximum path sum of testTree: {result}")

    
if __name__ == "__main__":
	main()

