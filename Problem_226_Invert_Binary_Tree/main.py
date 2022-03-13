from Solution import TreeNode, Solution

# Pass in root node of binary tree plus an array in which to collect them
def collectValuesInTree(root, collected):

    # Exit recursion when branch end is reached
    if not root:
        return None

    # Collect the value of the root node
    if len(collected) == 0:
        collected.append(root.val)
    
    # If branches exist, collect their values
    if root.left:
        collected.append(root.left.val)
    if root.right:
        collected.append(root.right.val)
    
    # If branches exist, recurse into them
    if root.left:
        collectValuesInTree(root.left, collected)
    if root.right:
        collectValuesInTree(root.right, collected)
    
    # Return the fully populated array
    return collected

def main():
    
    # Example 1
    # Create first list node and set the head pointer there
    treeNodeHead = testTree = TreeNode(4)
    testTree.left = TreeNode(2)
    testTree.right = TreeNode(7)
    testTree = testTree.left
    testTree.left = TreeNode(1)
    testTree.right = TreeNode(3)
    testTree = treeNodeHead
    testTree = testTree.right
    testTree.left = TreeNode(6)
    testTree.right = TreeNode(9)
    testTree = treeNodeHead

    # Example 2
    #treeNodeHead = testTree = TreeNode(2)
    #testTree.left = TreeNode(1)
    #testTree.right = TreeNode(3)

    # Example 3
    #treeNodeHead = testTree = TreeNode()

    # Instantiate Solution class
    s = Solution()

    # Run the solution
    answer = s.invertTree(testTree)

    allVals = []
    collectValuesInTree(answer, allVals)

    print("Print all values of inverted tree: ")
    print(allVals)


if __name__ == "__main__":
	main()

