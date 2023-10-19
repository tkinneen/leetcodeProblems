from Solution import TreeNode, Codec

def main():

    # Example 1
    #root = [1, 2, 3, "Null", "Null", 4, 5]
    root = "1,2,3,Null,Null,4,5"

    # Build test tree - Example 2
    treeNodeHead = testTree = TreeNode(1)
    testTree.left = TreeNode(2)
    testTree.right = TreeNode(3)
    testTree = testTree.right
    testTree.left = TreeNode(4)
    testTree.right = TreeNode(5)

    # Point to the head before passing to the Solution class
    root = treeNodeHead

    #Example 2:
    #root = []

    # Instantiate Solution class
    #s = Solution()

    # Your Codec object will be instantiated and called as such:
    ser = Codec()
    deser = Codec()
    result = deser.deserialize(ser.serialize(root))

    # Run the solution
    print(f"Result: {result}")


if __name__ == "__main__":
	main()

