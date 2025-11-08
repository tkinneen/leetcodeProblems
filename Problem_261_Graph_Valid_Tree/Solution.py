# LeetCode Problem 261: Graph Valid Tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
#    pair of nodes), write a function to check whether these edges make up a valid tree.

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A graph is a valid tree if:
        #   1.) All nodes are fully connected, and 
        #   2.) Its edges contain no cycles

        # Time: O(n + m) // Space: O(n + m)
        
        # Edge case - empty graph is technically a tree
        if not n:
            return True

        # Create a dictionary each node in the graph is represented by a unique int value, 
        #    and its pair is an array representing its adjacency list
        adjacency = { i:[] for i in range(n) }

        # Graph is undriected, so for each edge add a node's complement to it's adjacency list
        for node1, node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)

        # Track every node we traverse to
        visited = set()

        def dfs(i, prev):

            # Base case: if the node we've recursed into appears in the visited array, we've  
            #    seen it before and a cycle has been detected. This graph is not a valid tree.
            if i in visited:
                return False

            # The tree is still valid, so track it as visited
            visited.add(i)

            # Loop through all connections in the current node's adjacency list
            for j in adjacency[i]:
                
                # This node is the last one we visited and does not constitue a loop; 
                #   Jump to the next loop iteration
                if j == prev:
                    continue

                # Recurse further into the graph, passing the next node in the adjacency as
                #    the current and the current node as the "prev"
                # If the dfs function returns false, a loop was detected and the False will
                #    bubble up the recursion chain
                if not dfs(j, i):
                    return False

            # When running the DFS, the only False condition is a detected cycle
            return True

        # Kick off recursion and check that 1. there were no cycles and 2. that the total number of 
        #    nodes visited matches the number of nodes specified in the problem input
        # Passing 0 as the entry into the graph and a previous node as -1 as we know it doesn't exist, 
        #    so the condition will never hit
        return dfs(0, -1) and n == len(visited)