# LeetCode Problem 542: 01 Matrix
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two cells sharing a common edge is 1.

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # Time: O(m * n)
        # Memory: O(m * n)

        m, n = len(mat), len(mat[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Make a first pass over the entire grid, setting 1's to -1 so they are 
        #    not confused with actual distances, and adding all 0's to a queue so
        #    we can kick off our bfs
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    mat[row][col] = -1
                else:
                    q.append((row, col))

        # Perform inline bfs. Each -1 node you reach, use the previous node
        #    to calculate the current node's value. The nature of bfs ensures
        #    that if a node is -1, this is the fewest possible steps to have reached it
        while q:
            row, col = q.popleft()
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                if (
                    0 <= new_row < m and
                    0 <= new_col < n and
                    mat[new_row][new_col] == -1 
                ):
                    mat[new_row][new_col] = mat[row][col] + 1
                    # Append current q to check its neighbors. Though we started by adding
                    #    all 0's to the q, appended nodes can have any number of steps
                    q.append((new_row, new_col))
        return mat