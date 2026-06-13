# LeetCode Problem 695: Max Area of Island
#
# You are given an m x n binary matrix grid. An island is a group of 1's (representing 
#    land) connected 4-directionally (horizontal or vertical.) You may assume all four 
#    edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Iterative, breadth first search solution
        def bfs(r, c):
            # Initialize the q with the starting node
            q = deque([(r, c)])
            # Set the initial node to 0 so it doesn't get re-checked
            grid[r][c] = 0
            # Initialize the current area, representing the initial node
            area = 1
            while q:
                row, col = q.popleft()
                for row_offset, col_offset in directions:
                    new_row, new_col = row + row_offset, col + col_offset
                    if(
                        0 <= new_row < m and
                        0 <= new_col < n and 
                        grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 0
                        area += 1
                        q.append((new_row, new_col))
            return area      
        
        # Recursive, depth first search solution
        def dfs(r, c):
            # Base case
            if(
                0 > r or
                r >= m or
                0 > c or
                c >= n or 
                grid[r][c] != 1
            ):
                return 0
            
            # Process the node by setting it to 0, so it doesn't get checked again
            # If the interviewer says grid mutation is not allowed, use a visited set
            grid[r][c] = 0
            
            # initialize the current island's area value (representing the current node's area)
            cur_area = 1

            # Accumulate the area from all possible directions. Will return 0 if invalid
            cur_area += dfs(r - 1, c)
            cur_area += dfs(r + 1, c)            
            cur_area += dfs(r, c - 1)           
            cur_area += dfs(r, c + 1)
            
            # dfs has bubbled up the full area of the island, so return
            return cur_area
        

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    #cur_area = dfs(row, col)
                    # Perform a search on the land, checking the result area against the max so far
                    cur_area = bfs(row, col)
                    max_area = max(max_area, cur_area)
        return max_area