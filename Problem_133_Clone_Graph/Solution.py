# LeetCode Problem 133: Clone Graph
#
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its
#    neighbors.
#
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed).
#    For example, the first node with val == 1, the second node with val == 2,
#    and so on. The graph is represented in the test case using an adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a finite
#    graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the
#   copy of the given node as a reference to the cloned graph.
#
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":

        # Time complexity: O(v + e) where v is the number of verticies and e is 
        #    the number of edges. DFS traverses each node once, and each edge 
        #    of each node is explored
        # Space complexity: O(v)

        # Hash map to link original nodes their clones. Original node acts as the
        #    key to access the clone
        originalToNew = {}

        # This depth first search function performs several operations:
        #    1. If a node is passed in that already exists in our hash map, use 
        #       our map to return the existing clone
        #    2. If the node is not in the hash map, clone it by instantiating a 
        #       new Node object with its value
        #    3. After cloning it, loop through the neighbors array of the original 
        #       node and append each node it contains to the clone's neighbors array
        def dfs(node):

            # How this flows: Recursion starts and a node is cloned. Then the neighbors 
            #    of the original node are added to the clone through the dfs function.
            #    If a neighbor node hasn't been seen yet, it will clone THAT node before
            #    it finishes the original's neighbors, recursing potentially deeply before
            #    the original neighbor array is complete

            # If an original is passed in and has already been seen, return the
            #    already-created clone
            # "in" operator checks ONLY keys
            if node in originalToNew:
                return originalToNew[node]

            # Node has NOT been seen, so create a clone
            copy = Node(node.val)

            # Use the original as the key in our hash map to link it to the clone
            originalToNew[node] = copy

            # Iterate over all neighbor edges of the original node
            for curNeighbor in node.neighbors:

                # For each neighbor, run the dfs clone function on the node, and append what is returned to the copy's neighbors array
                #    New nodes will be added to the hash, and then their neighbor arrays will be populated before finishing the original node
                copy.neighbors.append(dfs(curNeighbor))

            # Return the full copy that was just created (new node with fully-populated neighbors)
            return copy

        # The return requires this protection if no nodes are passed in for the test case
        return dfs(node) if node else None