# 207. Course Schedule

## Problem Context
The goal is to determine if all courses can be finished given a set of prerequisites. This is equivalent to finding if a **Directed Cycle** exists in the graph of course dependencies.

## Cycle Detection Logic (DFS + Backtracking)

The solution uses Depth First Search (DFS) with a `visited` set to track the current recursion path. This is a common pattern for detecting cycles in directed graphs.

### The "Red Pin" Analogy 🚩
Imagine exploring a series of one-way tunnels in a cave with a bag of **Red Pins**:

1. **`visited.add(c)`**: When you enter course `c`, you stick a **Red Pin** on the wall. This marks that you are **currently investigating** this path.
2. **`visited.remove(c)`**: Once you have explored all branches leading from `c` and confirmed they don't loop back, you **take your Red Pin back** as you leave. This marks the node as "finished" for the current exploration.

### 💡 Why `visited.remove(c)` is Necessary?

Without removing the node from the `visited` set, the algorithm would incorrectly detect cycles in "V-shaped" or Diamond-shaped graphs where two different paths meet at the same safe node.

#### Example: The V-Shape
- Course **A** needs **C** (`A -> C`)
- Course **B** needs **C** (`B -> C`)

| Step | Action | `visited` set | Explanation |
| :--- | :--- | :--- | :--- |
| 1 | Visit **A** | `{A}` | |
| 2 | Visit **C** | `{A, C}` | |
| 3 | Finish **C** | `{A, C} -> {A}` | **`remove(C)`** allows future paths to visit C safely. |
| 4 | Finish **A** | `{A} -> {}` | |
| 5 | Visit **B** | `{B}` | |
| 6 | Visit **C** | `{B, C}` | **No loop!** Since C was removed from the set in Step 3. |

> [!IMPORTANT]
> If we did NOT remove **C** in Step 3, Step 6 would see `C` in `visited` and falsely report a cycle.

## Optimized Implementation

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visited = set()
        
        def dfs(c):
            if c in visited: # Cycle detected!
                return False
            if pre_map[c] == []: # Already confirmed safe
                return True
            
            visited.add(c)
            for pre in pre_map[c]:
                if not dfs(pre): # Check if sub-path is safe
                    return False
            
            visited.remove(c)
            pre_map[c] = [] # OPTIMIZATION: Mark as safe for other paths
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
```

### Key Optimizations
- **Redundant Call Fix**: Ensure `dfs(pre)` is only called once per dependency.
- **Memoization**: By setting `pre_map[crs] = []` after a successful visit, we prevent re-calculating the same safe branches multiple times, significantly improving performance for large test cases.
