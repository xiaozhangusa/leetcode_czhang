from typing import List
from collections import deque

# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 

# Constraints:

# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island = []
        
        # 1. find the 1st piece of land in the 1st island
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    found = True
                    break
            if found:
                break
        
        # 2. dfs to find all pieces of land in the 1st island and mark them as 2
        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = 2
            island.append((i, j))
            while stack:
                r, c = stack.pop()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    # push all neighbors to stack if they are land
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        island.append((nr, nc))
                        stack.append((nr, nc))

        dfs(first_x, first_y)
        
        # 3. bfs to find the shortest path to the 2nd island
        q = deque(island)
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return dist
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1  # mark as visited
                            q.append((nr, nc))
            dist += 1
        
        return dist
