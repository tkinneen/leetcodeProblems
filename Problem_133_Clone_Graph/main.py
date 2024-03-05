from Solution import Node, Solution

# Recursively prints all nodes in graphs, using a Set to skip duplicates
def printResultGraph(node, visited):
    if not node:
        print("Passed in node is Null")
        return
    if node not in visited:
        print(node.val)
        visited.add(node)
        for neighbor in node.neighbors:
            printResultGraph(neighbor, visited)

def main():
    # Example 1
    # Instantiate the nodes in the graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Connect edges of all neighbors
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    # Example 2
    # node1 = Node(1)

    #  Example 3
    # node1 = None

    # Instantiate Solution class
    s = Solution()

    # Returns a single node of the cloned graph that is fully connected to all other nodes
    result = s.cloneGraph(node1)

    # Initialize a set to recursively print the result graph
    visited = set()

    # Pass the result and the empty set to the recursive print function
    printResultGraph(result, visited)

if __name__ == "__main__":
    main()
