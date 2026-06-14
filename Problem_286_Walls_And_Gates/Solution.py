# LeetCode Problem 286: Walls and Gates
#
# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to 
#    represent INF as you may assume that the distance to a gate is less than 2147483647.
#
# Fill each empty room with the distance to its nearest gate. If it is impossible to 
#    reach a Gate, that room should remain filled with INF

from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        # Time: O(m * n) - Entire graph is traversed twice in worst case. Constants are dropped
        # Space: O(m * n)

        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Traverse the entire grid, adding all gates to the q
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))

        # Perform a standard inline bfs traversal, searching for in-bound rooms that
        #    have yet to be processed
        while q:
            row, col = q.popleft()
            for row_offset, col_offset in directions:
                new_row, new_col = row + row_offset, col + col_offset
                if (
                    0 <= new_row < m and
                    0 <= new_col < n and
                    rooms[new_row][new_col] == 2147483647
                ):
                    # If a room is infinity it hasn't been processed yet. Use the step count
                    #    of the adjacent node that preceeded it to calculate its count. Due
                    #    to the nature of bfs, when a new room is reached it is the shortest
                    #    possible distance to nearest gate
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    q.append((new_row, new_col))
        
        # This solution specifies a null return value, but for the purposes of this code base 
        #    we will return the modified room grid
        return rooms