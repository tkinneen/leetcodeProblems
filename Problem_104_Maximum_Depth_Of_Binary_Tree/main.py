from Solution import TreeNode, Solution

def main():
    
    # Build test tree
    treeNodeHead = testTree = TreeNode(3)
    testTree.left = TreeNode(9)
    testTree.right = TreeNode(20)
    testTree = testTree.right
    testTree.left = TreeNode(15)
    testTree.right = TreeNode(7)
    placeholder = testTree
    testTree = testTree.left
    testTree.left = TreeNode(77)
    testTree.right = TreeNode(88)
    testTree = placeholder
    testTree = testTree.right
    testTree.left = TreeNode(33)
    testTree.right = TreeNode(44)

    # Point to the head before passing to the Solution class
    testTree = treeNodeHead
    
    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.maxDepth(testTree)
    print("Max depth of the binary tree: " + str(answer))

    
if __name__ == "__main__":
	main()

