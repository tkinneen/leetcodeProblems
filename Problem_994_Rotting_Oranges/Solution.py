# LeetCode Problem 994: Rotting Oranges
#
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
#    becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh 
#    orange. If this is impossible, return -1.

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        rotten_q = deque()
        fresh_count = 0

        # Make a single pass through the entire grid, adding all rotten oranges to the
        #    initial queue and also keeping count of all fresh fruit
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten_q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        # Perform the breadth first search. Each "level" of the search, another minute passes
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0

        # Continue for as long as rotten fruit remain in the q.
        # If rotten oranges are still in the q but no fresh fruit remain, no need to proceed 
        while rotten_q and fresh_count > 0:
            for _ in range(len(rotten_q)):
                row, col = rotten_q.popleft()
                for row_offset, col_offset in directions:
                    new_row, new_col = row + row_offset, col + col_offset
                    if(
                        0 <= new_row < m and
                        0 <= new_col < n and
                        grid[new_row][new_col] == 1
                    ):
                        # If the current node is in range and contains a fresh orange, make it rotten,
                        #    decrement the fresh count and add the newly-rotten orange to the q
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        rotten_q.append((new_row, new_col))
            minutes += 1
        
        # If fresh oranges remain they are not reachable, so return -1
        return minutes if fresh_count == 0 else -1