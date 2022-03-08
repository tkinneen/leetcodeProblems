from Solution import TreeNode, Solution

def main():
    
    # Example 1
    # Create first list node and set the head pointer there
    treeNodeHead = testTree = TreeNode(2)
    testTree.left = TreeNode(1)
    testTree.right = TreeNode(3)

    # Example 2
    treeNodeHead = testTree = TreeNode(5)
    testTree.left = TreeNode(1)
    testTree.right = TreeNode(4)
    testTree = testTree.right
    testTree.left = TreeNode(3)
    testTree.right = TreeNode(6)
    testTree = treeNodeHead
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.isValidBST(testTree)
    print("This is a valid BST: ")
    print(answer)

    
if __name__ == "__main__":
	main()

