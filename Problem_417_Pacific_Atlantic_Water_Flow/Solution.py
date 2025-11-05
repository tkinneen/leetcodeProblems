# LeetCode Problem 417: Clone Pacific Atlantic Water Flow
#
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic
#    Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic
#    Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n integer
#    matrix heights where heights[r][c] represents the height above sea level of the 
#    cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells
#    directly north, south, east, and west if the neighboring cell's height is less 
#    than or equal to the current cell's height. Water can flow from any cell adjacent
#    to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
#    rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Time: O(m*n) - Technically O(2mn) since at worst we'll visit every cell twice
        # Space: O(m*n) - Technically O(4mn) as BFS requires both a deque and set for each ocean

        pacific_q = deque()
        pacific_seen = set()

        atlantic_q = deque()
        atlantic_seen = set()

        # Get the dimensions of the grid, split into rows and columns
        m, n = len(heights), len(heights[0])

        # Start by packing the pacific and atlantic queues with every cell that touches the ocean
        
        # Pacific northern border
        for j in range(n):
            pacific_q.append((0, j))
            pacific_seen.add((0, j))

        # Pacific western border - start range at 1 to not double-count top left corner
        for i in range(1, m):
            pacific_q.append((i, 0))
            pacific_seen.add((i, 0))

        # Atlantic eastern border
        for i in range(m):
            atlantic_q.append((i, n - 1))
            atlantic_seen.add((i, n - 1))
        
        # Atlantic southern border
        # (n - 1) skips the bottom-right node, and (m - 1) pins us to the bottom row
        for j in range(n - 1):
            atlantic_q.append((m - 1, j))
            atlantic_seen.add((m - 1, j))

        # This is a BFS function which will fan FROM all ocean-touching positions TO all
        #    positions are are capable of flowing into it
        def get_coords(q, seen):
            
            # This set will hold all the valid positions for the passed-in ocean
            coords = set()
            
            # Loop until all possible positions are exhausted
            while q:

                # Pop the current node off the q and add it to our result
                row, col = q.popleft()
                coords.add((row, col))

                # Get a row/column offset representing one of the 4 cardinal directions
                for row_offset, col_offset in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    
                    # Add the offset to our current node to get a new position to try
                    new_row, new_col = row + row_offset, col + col_offset
                    
                    # If the new node is in bounds, has not been seen, and can flow INTO
                    #    the current node, add it to the q and mark it seen
                    if(
                        0 <= new_row < m 
                        and 0 <= new_col < n 
                        and heights[new_row][new_col] >= heights[row][col] 
                        and (new_row, new_col) not in seen
                    ):
                        q.append((new_row, new_col))
                        seen.add((new_row, new_col))
            
            return coords
        
        # Call the BFS function on each of our ocean-adjacent queues, which will result in a 
        #    full set of flowable nodes to each ocean
        pacific_coords = get_coords(pacific_q, pacific_seen)
        atlantic_coords = get_coords(atlantic_q, atlantic_seen)

        # Return a single set (cast as a list) containing nodes that exist in both individual ocean sets
        return list(pacific_coords.intersection(atlantic_coords))