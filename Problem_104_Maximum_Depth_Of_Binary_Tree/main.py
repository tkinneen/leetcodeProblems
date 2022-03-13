from Solution import TreeNode, Solution

def main():
    
    # Example 1
    # Create first list node and set the head pointer there
    treeNodeHead = testTree = TreeNode(3)
    testTree.left = TreeNode(9)
    testTree.right = TreeNode(20)
    testTree = testTree.right
    testTree.left = TreeNode(15)
    testTree.right = TreeNode(7)
    testTree = treeNodeHead
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.maxDepth(testTree)
    print("Max depth of binary tree: " + str(answer))

    
if __name__ == "__main__":
	main()

