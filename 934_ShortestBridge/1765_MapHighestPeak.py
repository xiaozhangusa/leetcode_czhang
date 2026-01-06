# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

# Example 1:



# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.
# Example 2:



# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        if not isWater or not isWater[0]:
            return []
        m, n = len(isWater), len(isWater[0])
        # height matrix initialized to 0
        ht = [[0] * n for _ in range(m)]
        print("ht: ", ht)
        # find all water cells and add them to the queue
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        h = -1
        while q:
            h += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                ht[r][c] = h
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and isWater[nr][nc] == 0:
                        isWater[nr][nc] = 1
                        q.append((nr, nc))
        return ht

        
        