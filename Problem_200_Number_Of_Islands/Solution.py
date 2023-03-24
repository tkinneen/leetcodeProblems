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
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        print("range(rows):")
        print(range(rows))
        print("range(cols):")
        print(range(cols))
        visited = set()
        islands = 0

        def breadthFirstSearch(r, c):
            print("bfs initiating...")
            print("================")
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                print("q at the top of the while: ")
                print(q)
                row, col = q.popleft()
                print(f"row: {row}, col: {col}")
                print(f"Value at this position: {grid[row][col]}")
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr__, dc__ in directions:
                    r, c = row + dr__, col + dc__
                    print(f"Checking direction - r: {r}, c: {c}")
                    print(f"value at the positon we're checking: {grid[r][c]}")
                    if(grid[r][c] == "1"):
                        print("This is a VALID island")
                    else:
                        print("This is NOT a valid island")
                    if((r, c) in visited):
                        print("NOT adding to q, already visited")
                    else:
                        print("Already visited, skipping...")
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        print(f"Adding ({r}, {c}) to the q")
                        q.append((r, c))
                        visited.add((r, c))
                print("=========")

        for curRow in range(rows):
            for curCol in range(cols):
                if grid[curRow][curCol] == "1" and (curRow, curCol) not in visited:
                    breadthFirstSearch(curRow, curCol)
                    islands += 1
        return islands
