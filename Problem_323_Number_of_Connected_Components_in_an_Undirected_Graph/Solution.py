# LeetCode Problem 323: Number of Connected Components in an Undirected Graph 
#
# You have a graph of n nodes. You are given an integer n and an array of edges
#    where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
#    in the graph. 
#
# Return the number of connected components in the graph

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # This algorithm is called a "Disjoint Set Data Structure" or "DSU - Disjoint Set Union"

        # Time: O(N + E), where N is the number of nodes and E is the number of edges
        # Space: O(V) == O(2V) (two arrays each the size of the number of nodes)
        # Technically the time complexity is O((N + E) * α(N)), where a(N) is a inverse Ackermann function that grows insanely slowly 
        
        # List comprehension creates an array of sequential elements from 0 to n-1, each one representing a node.
        # Each element in the parent array can also be thought of as a "representative" of all the connected nodes in a graph.
        # Before connection, each individual node points to itself; it's its own representative
        parent = [i for i in range(n)]
        
        # Rank array has an element for each node, all starting at 1. Rank is tracked by
        #    parent nodes, and represents magnitude of the graph's connections
        rank = [1] * n

        # Finds the representative node 
        def find(n1):
            result = n1

            # Until the graph's parent is found, continually shift from node to parent node
            while result != parent[result]:
                
                # Path compression: chain-shaped graphs jump their parent to their
                #    grandparent to converge on the parent node for faster finds   
                parent[result] = parent[parent[result]]

                result = parent[result]

            # result = parent of the graph
            return result
        
        # Either joins two nodes and returns 1, or returns 0 if they're already in the same graph
        def union(n1, n2):

            # First find the parent of both nodes
            p1, p2 = find(n1), find(n2)

            # No join needed; graphs are already connected
            if p1 == p2:
                return 0
            
            # The parent of higher rank will become the lesser node's parent
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                # The dominant node's rank add's the lesser node's magnitude to its own
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            # Because a join occurred, this will decrement the result counter 
            return 1
        
        # Start with the total number of nodes, assuming none are connected
        result = n

        # Loop through all edges, one pair at a time
        for n1, n2 in edges:
            
            # If a union is performed, decrement the result
            result -= union(n1, n2)
        
        return result
        