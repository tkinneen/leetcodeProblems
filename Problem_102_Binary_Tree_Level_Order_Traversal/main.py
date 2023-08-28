from Solution import TreeNode, Solution

def main():
    
    # Test Case 1 - Output: [[3],[9,20],[15,7]]
    treeNodeHead = testTree = TreeNode(3)
    testTree.left = TreeNode(9)
    testTree.right = TreeNode(20)
    testTree = testTree.right
    testTree.left = TreeNode(15)
    testTree.right = TreeNode(7)
    testTree = treeNodeHead

    # Test Case 2 - Output: [[1]]
    #testTree = TreeNode(1)

    # Test Case 3 - Output: []
    #testTree = TreeNode(None)
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    result = s.levelOrder(testTree)
    print(f"Values contained in binary tree, ordered by level: {result}")

    
if __name__ == "__main__":
	main()

