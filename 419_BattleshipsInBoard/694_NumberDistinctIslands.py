# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

# Return the number of distinct islands.

 

# Example 1:


# Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# Output: 1
# Example 2:


# Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        distinctIsland = {}
        visited = [[False] * n for _ in range(m)]
        curIsland = []
        cnt = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            visited[i][j] = True
            if grid[i][j] == 1:
                curIsland.append((i, j))
            # stack
            s = [(i, j)]
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while s:
                r, c = s.pop()
                # extend to four dirs one by one
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    s.append((nr, nc))
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    if curIsland not in distinctIsland:
                        distinctIsland[curIsland] += 1
                    curIsland = []
        return cnt