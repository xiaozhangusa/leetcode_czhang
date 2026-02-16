# 🌊 BFS Mastery: The "Ripple" Pattern

Breadth-First Search (BFS) is the most intuitive way to explore a network. Think of it as **dropping a pebble into a calm pond.**

## 🧠 The Mental Model: The Pond Ripple

- **The Pebble**: Your starting node.
- **The Ripple**: The search frontier. It expands outward in perfect concentric circles.
- **The Levels**: Everything in the first ripple is 1 step away. Everything in the second ripple is 2 steps away.
- **Shortest Path**: Because we explore level-by-level, the **first time** you see a target, it is guaranteed to be the shortest path.

---

## 🏗️ Template 1: Iterative BFS (The Gold Standard)

This is the most common version. It's iterative, using a `deque` (queue) to manage the ripples.

### The "Level-by-Level" Snapshot
We use a nested `for` loop to process one full ripple at a time. This is critical for counting steps/levels.

```python
from collections import deque

def bfs_standard(root):
    if not root: return
    
    # 1. Initialize Queue & Visited (Discovery Phase)
    queue = deque([root])
    visited = {root} # Mark as visited IMMEDIATELY
    level = 0
    
    while queue:
        # 2. Level Snapshot: Process ONE full ripple
        nodes_at_this_level = len(queue)
        for _ in range(nodes_at_this_level):
            curr = queue.popleft()
            
            # 3. Target Check
            if is_target(curr):
                return level
            
            # 4. Expansion (Discovery)
            for neighbor in get_neighbors(curr):
                if neighbor not in visited:
                    visited.add(neighbor) # Lock it down now!
                    queue.append(neighbor)
        
        # 5. Move to next ripple
        level += 1
```

---

## 🏗️ Template 2: Recursive BFS (The Depth-Tracking DFS)

> [!NOTE]
> Strictly speaking, BFS is iterative by nature because recursion uses a **Stack** (LIFO), which is the opposite of a **Queue** (FIFO).
> However, we can simulate BFS results (finding level averages, printing by level) using a **Recursive DFS** that tracks the current level.

### Mental Model: The "Postal Carrier"
Imagine a postal carrier. Instead of processing level 1 then level 2, the carrier visits every house (DFS) but carries a **level tag**. Every time they arrive at a house, they put the mail into the specific "Level Bin" associated with that house's distance from the post office.

```python
def bfs_recursive_simulation(node, level, results):
    if not node: return
    
    # If this is our first time reaching this depth, create a new bin
    if level == len(results):
        results.append([])
    
    # Put the node in its corresponding level bin
    results[level].append(node.val)
    
    # Recursive step (Standard DFS, but level-aware)
    bfs_recursive_simulation(node.left, level + 1, results)
    bfs_recursive_simulation(node.right, level + 1, results)

# To use:
# levels = []
# bfs_recursive_simulation(root, 0, levels)
```

---

## 🏗️ Template 3: Deterministic Path Verification (The "Trail Follower")

In some problems (like the **Knight Tour**), you aren't searching for *any* path; you are verifying a **specific, pre-defined trail** of numbers or steps using neighbor rules.

### Mental Model: The breadcrumb trail
Instead of ripples, imagine you are a detective following breadcrumbs labeled `1, 2, 3...`. At each step, you check the valid "moves" allowed by the board to see if the next breadcrumb is exactly where it's supposed to be.

```python
def verify_sequential_path(grid, start_pos):
    n = len(grid)
    cx, cy = start_pos
    
    # Follow the numbers from 1 to n*n-1
    for move in range(1, n * n):
        found = False
        for dx, dy in get_neighbor_rules():
            nx, ny = cx + dx, cy + dy
            
            # Check the "Invisible Fence" and the next number
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == move:
                cx, cy = nx, ny # Move the detective to the next breadcrumb
                found = True
                break
        
        if not found: # Trail is broken!
            return False
            
    return True
```

---

## ⚡ Comparison & Choose Wisely

| Feature | Iterative BFS | Recursive Simulation | Path Verification |
| :--- | :--- | :--- | :--- |
| **Data Structure** | Queue (FIFO) | Call Stack (LIFO) | Loop variables (`cx, cy`) |
| **Shortest Path** | Perfect! Stops early. | Not efficient for early stop. | N/A (Path is fixed) |
| **Complexity** | $O(V+E)$ | $O(N)$ for trees. | $O(\text{Sequence Length})$ |
| **Best For** | Minimum steps, Shortest path. | Tree level-order stats (avg, max). | Validating a specific sequence. |

---

## 📚 Must-Do Representative Problems

### 1. Standard Iterative (The Fundamentals)
*   **[LC 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)**: The baseline for level-by-level processing.
*   **[LC 116. Populating Next Right Pointers](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)**: Using level context to connect nodes.

### 2. Shortest Path & Grid Exploration
*   **[LC 1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)**: Classic shortest path on an infinite board (the problem that started this guide!).
*   **[LC 127. Word Ladder](https://leetcode.com/problems/word-ladder/)**: A high-difficulty shortest path in a graph of string transformations.

### 3. Multi-Source BFS (The "Parallel Ripple")
*   **[LC 994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)**: Starting ripples from multiple locations simultaneously.
*   **[LC 542. 01 Matrix](https://leetcode.com/problems/01-matrix/)**: Finding distances to the nearest target for every cell.

### 4. Bidirectional BFS (The Optimization)
*   **[LC 127. Word Ladder](https://leetcode.com/problems/word-ladder/)**: Often required for optimal performance on this problem.
*   **[LC 433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)**: Another great candidate for meeting in the middle.

### 5. Level-Aware Recursion (DFS Simulating BFS)
*   **[LC 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)**: Often cleaner with level-aware recursion.
*   **[LC 637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)**: Perfect for accumulating stats per level.

### 6. Deterministic Path Verification (The Detective)
*   **[LC 2596. Check Knight Tour Configuration](https://leetcode.com/problems/check-knight-tour-configuration/)**: Validating a sequential breadcrumb trail on a grid.
*   **[LC 331. Verify Preorder Serialization](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)**: Verifying if a sequence follows tree structure rules.

---

## ⛵ Vivid Examples

### Example A: The Viral Post (Shortest Path)
**Goal**: Find the minimum degree of separation between You and a Celebrity.
- **BFS**: You check your friends (Level 1), then their friends (Level 2). The moment you hit the Celebrity, you stop. You found the literal "Six Degrees of Separation."

### Example B: The Flash Flood (Flood Fill)
**Goal**: You have a leak in a room. Which tiles get wet first?
- **BFS**: The tiles adjacent to the leak (Level 1) get wet simultaneously, then the ones adjacent to those (Level 2).

---

## 🚀 Pro-Tip: The "Visited" Rule
Remember: **Mark it as visited when you DISCOVER it (append), not when you PROCESS it (pop).** Otherwise, your pond ripples will turn into a chaotic storm!
