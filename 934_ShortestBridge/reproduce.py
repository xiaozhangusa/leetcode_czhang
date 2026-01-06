from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        # 1. find all pieces of land connected to the pacific ocean
        # 2. find all pieces of land connected to the atlantic ocean
        # 3. find the intersection of the two sets
        pacific = set()
        atlantic = set()
        m, n = len(heights), len(heights[0])
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n-1))
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m-1, j))
        # bfs to find all pieces of land connected to the pacific ocean
        def bfs(q):
            visited = set()
            reachable = set()
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    reachable.add((r, c))
                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in reachable and heights[nr][nc] > heights[r][c]:
                            q.append((nr, nc))
            return reachable
        
        # bfs to find all pieces of land connected to the atlantic ocean
        p_reachable = bfs(deque(pacific))
        a_reachable = bfs(deque(atlantic))
        return list(p_reachable & a_reachable)

if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    output = sol.pacificAtlantic(heights)
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    
    # Convert to sets of tuples for comparison
    output_set = set(tuple(x) for x in output)
    expected_set = set(tuple(x) for x in expected)
    
    print(f"Output: {sorted(list(output_set))}")
    print(f"Expected: {sorted(list(expected_set))}")
    
    assert output_set == expected_set, f"Failed! Missing: {expected_set - output_set}, Extra: {output_set - expected_set}"
    print("Test Passed!")
