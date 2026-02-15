# 210. Course Schedule II

## Problem Context
The goal is to provide a valid ordering of all courses given their prerequisites. If no such ordering exists (cycle detected), return an empty list.

---

## BFS (Kahn's Algorithm): The "Leveling Up" Approach 🕹️

Kahn's algorithm is generally the **most suitable** implementation for this problem because it builds the result naturally from the first course to the last.

### Why BFS Wins here:
1.  **Direct Order**: It naturally finds the "Starter Skills" (0-indegree) and appends them. No reversal needed.
2.  **No Recursion Risk**: Safely handles deep graphs without hitting Python's recursion limit.
3.  **Clean Logic**: Cycle detection is baked-in. If the final result size < `numCourses`, there’s a cycle.

---

## DFS (Post-Order): The "Deep Diver" 🤿

DFS builds the result from the **end to the beginning**. It finds the "absolute last thing you'll ever do" first.

### The Dual-Set Logic: `cycle` vs `visited`
In the DFS version, we use two separate concepts to manage the search.

| Set | Analogy | Meaning | Removal |
| :--- | :--- | :--- | :--- |
| **`cycle`** | **The Red Pin** 🚩 | "I am **currently standing** in this room." | **YES** (unhook when leaving). |
| **`visited`**| **The Safe Stamp** 🛡️| "I have **finished checking** everything here."| **NO** (keep as memo). |

#### Why both are needed?
- **Without `cycle`**: You cannot detect loops (Current Path tracking).
- **Without `visited`**: Your code will re-check the same "safe" branches over and over, leading to **Exponential Time** complexity (Pruning).

### DFS Implementation
```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build Adjacency List (pre -> [courses])
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            
        res = []
        visited = set() # Global safety stamp
        on_path = set() # Current path (tied string)

        def dfs(c):
            if c in on_path: # Loop detected!
                return False
            if c in visited: # Already confirmed safe
                return True
                
            on_path.add(c)
            for neighbor in adj[c]:
                if not dfs(neighbor):
                    return False
            
            on_path.remove(c)
            visited.add(c)
            # Post-order: add to result after exploring all neighbors
            res.append(c) 
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        # In DFS, we found the "end" of the paths first.
        # So we must reverse the list to get the order from start to finish.
        return res[::-1]
```

### Two Ways to Orient the DFS
There are two ways to model the relationships. Both are correct, but they change whether you need to reverse the result.

#### Approach A: Forward Edges (`pre -> course`)
This is the "textbook" way. You build the graph showing where a course leads.
- **Logic**: "I'm done with the prerequisite; what can I take now?"
- **Format**: `adj[pre].append(course)`
- **Result**: You find the "last" courses first. **Must reverse** at the end.

#### Approach B: Backward Edges (`course -> pre`) ⭐ *Your version*
This is a very clever way to avoid the reversal step. You build the graph showing what a course requires.
- **Logic**: "I want to take this course; what must I do first?"
- **Format**: `adj[course].append(pre)`
- **Result**: Post-order traversal finds the prerequisites first and appends them. Since prerequisites effectively "finish" before the main course, the list is **already in the correct order**.

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Backward Edges: course -> list of its prerequisites
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            
        res = []
        visited, on_path = set(), set()
        
        def dfs(crs):
            if crs in on_path: return False   # Path loop (Cycle)
            if crs in visited: return True  # Already certified safe
            
            on_path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            
            on_path.remove(crs)
            visited.add(crs)
            res.append(crs) # Post-order: Prereqs are added BEFORE the course
            return True
            
        for c in range(numCourses):
            if not dfs(c): return []
            
        return res # NO REVERSE NEEDED
```

### 🛡️ Why Pruning is Essential (The `visited` Set)
You'll notice the line `if crs in visited: return True`. This is **Memoization-based Pruning**.

- **The Problem**: Without this line, in a complex graph (like a "Diamond"), you would re-explore the same sub-branches millions of times.
- **The Solution**: 
    - **`cycle` (Red Pin)**: Tracks your *current* path to find loops.
    - **`visited` (Safe Stamp)**: Tracks your *global history* of safe nodes. 
- **The Analogy**: You climb a branch, check every twig, and find no rot. You put a "Certified Healthy" sign at the base of the branch. If you ever encounter that branch again from a different path, you see the sign and **stop (prune)** your search right there.

This turns an **Exponential** search process into a **Linear $O(V + E)$** one.

---

## Direct Comparison

| Feature | BFS (Kahn's) | Recursive DFS |
| :--- | :--- | :--- |
| **Logic** | "What can I learn **next**?" | "What must I do **before** this?" |
| **Intuition** | Forward-moving. Very clear. | Backward-moving. Bit abstract. |
| **Early Exit**| Slower (realizes late). | Faster (stops instantly on loop). |
| **Result Order**| Immediate. | Needs reversal (usually). |

### Summary Recommendation
Use **Kahn's (BFS)** for this problem. It is much more idiomatic for "ordering" tasks and avoids the complexity of manual backtracking and post-order sorting.
