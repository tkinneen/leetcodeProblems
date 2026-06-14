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

        # Time: O(m * n)
        # Space: O(m * n)

        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten_q = deque()
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Make a full pass over the grid, counting fresh oranges and enqueueing
        #    rotten ones in preparation for a bfs
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten_q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        # 
        # If no fresh oranges remain while rotten oranges are still in the q there 
        #    is no reason to proceed further
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
                        # Infect the current orange and decrement the "fresh" counter by 1
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        # Append the newly-rotten orange to the q
                        rotten_q.append((new_row, new_col))
            minutes += 1
        
        # Fresh fruit remain; Total infection is impossible
        if fresh_count:
            return -1
        
        # Return the number of minutes before all oranges are infected
        return minutes