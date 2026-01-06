from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island = []
        # 1. find the 1st piece of land in the 1st island
        first_x, first_y = -1, -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    # break # Only breaks inner loop
        
        def dfs(i: int, j: int) -> None:
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                    continue
                grid[i][j] = 2
                island.append((i, j))
                for cur_i, cur_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    # Missing boundary check here in original? 
                    # Wait, the original code had:
                    # if grid[cur_i][cur_j] == 1:
                    # That would crash if cur_i/cur_j are out of bounds.
                    if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                        if grid[cur_i][cur_j] == 1:
                            stack.append((cur_i, cur_j))
                            break # This is the "aggressive" break that is likely the bug

        # 2. dfs to find all pieces of land in the 1st island
        dfs(first_x, first_y)
        
        # 3. bfs to find the shortest path to the 2nd island
        q, frontier, dis = deque(island), [], 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for cur_i, cur_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                        if grid[cur_i][cur_j] == 1:
                            return dis
                        elif grid[cur_i][cur_j] == 0:
                            grid[cur_i][cur_j] = -1
                            frontier.append((cur_i, cur_j))
            q = deque(frontier)
            frontier = [] # I added this, but user DID NOT have it? 
            # Looking at original: line 44 `q, frontier, dis = deque(island), [], 0`
            # Line 54: `q = deque(frontier)`
            # User didn't clear frontier.
            dis += 1
        return dis

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,0,1,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
    try:
        result = sol.shortestBridge(grid)
        print(f"Result: {result}")
        expected = 1
        if result == expected:
            print("Success!")
        else:
            print(f"Failure! Expected {expected}, got {result}")
    except Exception as e:
        print(f"Error: {e}")
