# LeetCode Problem 261: Graph Valid Tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
#    pair of nodes), write a function to check whether these edges make up a valid tree.

from typing import List
from collections import deque

class Solution:
    def validTree(self, n, edges):

        # A graph is a valid tree if it's
        #   1.) Fully connected, and 
        #   2.) Contains no cycles

        # Time:  O(n + m)
        # Space: O(n + m)
        if not n:
            return True

        #
        adjacency = { i:[] for i in range(n) }

        #graphMap = {}
        #for i in range(n):
        #    graphMap[i] = []

#
        for node1, node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in adjacency[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False

            return True

        #
        return dfs(0, -1) and n == len(visited)