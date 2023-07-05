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
        # Time and space complexity are O(n * m), with n and m being the number of rows and columns
        #    This is because we must traverse every node in the grid
        # Memory could be reduced by getting rid of the "visited" Set by changing the value
        #    of a visited node to "0" once we've seen it, but this would involve
        #    modifying the input grid. Clarify with interviewer if that is allowed

        # Edge case - empty grid
        if not grid:
            return 0

        # Get the dimensions of the grid
        #   Each grid is an array of arrays, with each subarray containing a row
        rows, cols = len(grid), len(grid[0])

        # Keep track of already-traversed nodes with a Set object
        visited = set()
        islands = 0

        # Checks all surrounding nodes from a starting node until all connected "land" is fully explored
        def breadthFirstSearch(r, c):
            q = deque()

            # If BFS function engaged the current node is valid, so add to q and visited set
            visited.add((r, c))
            q.append((r, c))

            # Loop until the q is empty, at which point the current "island" is fully explored
            while q:
                # This deque will process nodes in the order they were added
                #    Note: popping from the right here will make this an iterative Depth First Search
                row, col = q.popleft()

                # Adding each of the below values to the current node will check a cardinal adjacent node
                # Corresponds to down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Check all directons specified above
                for rowDirChange, colDirChange in directions:
                    # Add direction change to the current row/col to move
                    r, c = row + rowDirChange, col + colDirChange

                    # Perform same island/visited check as the main function, but this time add range checks becuase
                    #    as the new directions could land outside the grid bounds
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        # If all above checks are valid append to the q and run the next iteration
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

        # The grid has been fully traversed, return the number of islands found
        return islands
