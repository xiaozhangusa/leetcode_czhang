# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# Return the number of pairs of different nodes that are unreachable from each other.

 

# Example 1:


# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
# Example 2:


# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each other:
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.
 

# Constraints:

# 1 <= n <= 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated edges.

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # find(x) returns the root of x, not the parent
        def find(x):
            if parent[x] != x:
                # compression recursively. find(parent[x]) finds the root of parent[x]
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # union by rank - smaller rank goes under larger rank
                if rootX > rootY:
                    rootX, rootY = rootY, rootX
                parent[rootY] =rootX
        
        # make set
        parent = list(range(n))
        for e in edges:
            union(e[0], e[1])
        
        # count number of nodes in each set
        cnt = Counter(find(i) for i in range(n))

        # count number of unreachable pairs
        ans = n * (n-1) // 2
        for c in cnt.values():
            # remove number of pairs within each set, c^2 because each node is counted twice
            ans -= c * (c-1) // 2
        return ans