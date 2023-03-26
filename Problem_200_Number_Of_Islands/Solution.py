# LeetCode Problem 200: Number of Islands
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
#    and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands 
#    horizontally or vertically. You may assume all four edges of the grid 
#    are all surrounded by water.

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Time complexity is O(n) - Space complexity is O(2n) as we have a deque 

        # Edge case - empty grid
        if not grid:
            return 0
        
        # Get the dimensions of the grid 
        #   Each grid is an array of arrays, with each subarray containing a row
        rows, cols = len(grid), len(grid[0])
        
        # Keep track of already-traversed nodes with a Set struct
        visited = set()
        islands = 0

        # From a starting node, checks every adjacent node for "land" until fully explored 
        def breadthFirstSearch(r, c):
            q = deque()
            # If we got here, current node is valid, so add to q/visited
            visited.add((r, c))
            q.append((r, c))
            
            # Loop until the q is empty, at which point the current "island" is fully explored
            while q:
                # Deque will process nodes in the order they were added
                #    Note: popping from the right here will make this a Depth First Search
                row, col = q.popleft()
                
                # Adding these values to the current node will check cardinal adjacent nodes
                # Corresponds to down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Check all directons specified above
                for rowDirection, colDirection in directions:
                    # Apply the current direction change to the current node
                    r, c = row + rowDirection, col + colDirection
                    
                    # Perform same island/visited check as the main function, but becuase we're 
                    #    checking all 4 directions around each node, a range check must also be done
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        # This nested for loop will traverse every node in the grid
        for curRow in range(rows):
            for curCol in range(cols):
                # If the current node is "land" and we haven't seen it yet, initiate BFS search
                #    and increment the island count
                if grid[curRow][curCol] == "1" and (curRow, curCol) not in visited:
                    breadthFirstSearch(curRow, curCol)
                    islands += 1
                    
        return islands