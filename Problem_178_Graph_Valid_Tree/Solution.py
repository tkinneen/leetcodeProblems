# LeetCode Problem 178: Graph Valid Tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each 
#    edge is a pair of nodes), write a function to check whether these edges 
#    make up a valid tree.

class Solution:
    def valid_tree(self, n, edges):
        
        # Time: O(e + v) (number of edges + number of vertices)
        # Space: O(e + v)

        # Graph is still valid if no nodes are passed in
        if not n:
            return True
        
        # Initialize an "adjacency list" map, an empty array for each node to 
        #    track the nodes that connect to it
        adjacencyList = { i:[] for i in range(n) }
        
        # Because the edges go both ways, add the current connection to the 
        #    adjacency list of both nodes the edge contains 
        for node1, node2 in edges:
            adjacencyList[node1].append(node2)
            adjacencyList[node2].append(node1)
        
        # Create a set to track each node we've visited
        visited = set()
        
        # Define the depth first search function, which has access to the adjacency list
        #    Arguments are the current node, and the previous node we just came from
        def dfs(currentNode, previousNode):
            
            # Base case: when a node exists in visited, it means there is a cycle and 
            #    the tree is NOT valid
            if currentNode in visited:
                return  False
            
            # This node has not been visited, so add it to the set
            visited.add(currentNode)

            # Loop through every node adjacent to the current node
            for currentNeighbor in adjacencyList[currentNode]:
                
                # Simply never recurse into the previous node, as it would break our 
                # use the continue statement to skip this iteration of the loop
                if currentNeighbor == previousNode:
                    continue
                
                # Recurse into the tree, bubbling up a False if a cycle is detected
                if not dfs(currentNeighbor, currentNode):
                    return False
            
            
            # If the entire tree has been traversed without returning, then 
            #    it is valid
            return True
        
        # Kick off recursion, performing the depth first search to ensure no 
        #    cycles exist. We pass -1 for the root's prev node as our node count
        #    starts at 0 and it will never be hit
        # The second check is necessary to ensure all the nodes in the graph were 
        #    visited, as unconnected nodes would make it invalid
        return dfs(0, -1) and n == len(visited)
    