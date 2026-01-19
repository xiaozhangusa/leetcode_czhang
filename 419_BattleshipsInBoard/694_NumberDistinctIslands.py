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
        # if not grid or not grid[0]:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # visited = [[False] * n for _ in range(m)]
        # islands = set()

        # def dfs(r, c, direction, signature):
        #     visited[r][c] = True
        #     signature.append(direction)
            
        #     # Explore Down, Up, Right, Left in a consistent order
        #     for dr, dc, d_char in [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]:
        #         nr, nc = r + dr, c + dc
        #         if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
        #             dfs(nr, nc, d_char, signature)
            
        #     # The "Vivid" part: Append '0' when backtracking
        #     signature.append('0')

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1 and not visited[i][j]:
        #             path = []
        #             dfs(i, j, 'S', path) # 'S' for Start
        #             islands.add("".join(path))
                    
        # return len(islands)

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        islands = set()
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, d, signature):
            visited[r][c] = True
            signature.append(d)
            for dx, dy, d in [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]:
                nr, nc = r + dx, c + dy
                print("nr, nc: ", nr, nc)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc, d, signature)
            path.append('0')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, 'S', path)  # use 'S' to mark start
                    path = "".join(path)
                    islands.add(path)
        return len(islands)
