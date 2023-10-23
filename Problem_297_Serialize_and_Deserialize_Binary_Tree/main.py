from Solution import TreeNode, Codec

def main():

    # Build test tree - Example 1
    treeNodeHead = testTree = TreeNode(1)
    testTree.left = TreeNode(2)
    testTree.right = TreeNode(3)
    testTree = testTree.right
    testTree.left = TreeNode(4)
    testTree.right = TreeNode(5)

    # Point to the head before passing to the Solution class
    root = treeNodeHead

    #Example 2:
    #root = None

    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    result = deser.deserialize(ser.serialize(root))

    # Run the solution
    print(f"Result: {result}")


if __name__ == "__main__":
	main()

