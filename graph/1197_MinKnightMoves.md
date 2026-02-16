# 1197. Minimum Knight Moves

## Problem Description
In an infinite chess board with coordinates from `-infinity` to `+infinity`, you have a knight at square `[0, 0]`. A knight has 8 possible moves. Return the minimum number of steps needed to move the knight to the square `[x, y]`.

---

## 🚀 Core Optimizations (First Quadrant Strategy)

#### 🔍 Detailed Example: The "Redundancy Explosion"
Imagine the knight is at **Level 0: (0, 0)**.

1.  **Level 1 Expansion**:
    The knight moves to 8 positions: `(2, 1), (1, 2), (-1, 2), (-2, 1), ...`
    All these nodes are now in the `q`. **None of them are in `visited` yet** because they haven't been popped.

2.  **Level 2 Explosion**:
    -   `Pop (2, 1)`: It sees it can move to **(3, 3)**. It checks `if (3, 3) not in visited`. It's not, so it appends **(3, 3)** to `q`.
    -   `Pop (1, 2)`: It ALSO sees it can move to **(3, 3)**. It checks `if (3, 3) not in visited`. Since **(3, 3)** hasn't been popped yet, it's *still* not in `visited`.
    -   **Result**: `(3, 3)` is added to the queue a **second time**.

3.  **The Exponential Chain Reaction**:
    In a knight's board, after just a few levels, there are **dozens of different paths** to reach the same coordinate.
    -   If you wait to mark a node as `visited` until you **pop** it, every single one of those dozens of paths will add that coordinate to the queue.
    -   By the time you reach the next level, those "dozens" become "thousands".
    -   Your queue length becomes proportional to the **number of paths to a node** (exponential), rather than the **number of unique nodes visited** (polynomial).

#### Visualization
| Point in Time | Queue (`q`) | Visited (`v`) |
| :--- | :--- | :--- |
| **Start** | `[(0,0)]` | `{}` |
| **Popping (0,0)** | `[(2,1), (1,2), ...]` | `{(0,0)}` |
| **Popping (2,1)** | `[(1,2), ..., (3,3)]` | `{(0,0), (2,1)}` |
| **Popping (1,2)** | `[..., (3,3), (3,3)]` | `{(0,0), (2,1), (1,2)}` |
| | **^ Redundancy!** | |

**The Fix** is to mark as visited **at the moment of discovery** (when appending). This effectively "locks" the coordinate so no other path can add it to the queue again.
To solve this efficiently on an "infinite" board, we use two mathematical tricks to collapse the search space:

### 1. Symmetry with `abs(x), abs(y)`
The board is perfectly symmetric. The path to `(2, 1)` is the same length as the path to `(-2, 1)`.
- **Action**: We treat all targets as if they are in the **first quadrant**.
- **Benefit**: Reduces the search area to 1/4th of the original size.

### 2. The "Knight's Hook" (`nx >= -1, ny >= -1`)
If we target `(1, 1)`, the shortest path is `(0,0) -> (2,-1) -> (1,1)`.
- **Action**: We allow the knight to step slightly into negative territory (`-1` or `-2`).
- **Benefit**: Prevents the search from missing the optimal path while still keeping it from wandering into infinity.

---

## 🐢 1. Standard BFS (Level-by-Level)

### The Elegance of the Level Loop
Processing the queue level-by-level ensures you find the **shortest** path and can count steps precisely.

```python
while q:
    for _ in range(len(q)):  # Captures a "snapshot" of the level
        curr_x, curr_y = q.popleft()
        # process...
    step += 1
```
- **Why it works**: `range(len(q))` is evaluated only once at the start of the `for` loop. Any nodes added during the loop wait until the next `while` iteration.

### Correct BFS Implementation
```python
from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        q = deque([(0, 0)])
        visited = {(0, 0)}
        step = 0
        
        while q:
            for _ in range(len(q)):
                cx, cy = q.popleft()
                if cx == x and cy == y: return step
                
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) not in visited and nx >= -1 and ny >= -1:
                        visited.add((nx, ny)) # <-- Add IMMEDIATELY
                        q.append((nx, ny))
            step += 1
        return -1
```

> [!WARNING]
> ### The TLE Trap: Late Visited Update
> If you add to `visited` **only when popping** (instead of when appending), the same coordinate can be added to the queue **hundreds of times** before the first one is actually processed. This causes an memory explosion and **Time Limit Exceeded (TLE)**.

#### Buggy Implementation (Your Original Version)
```python
x, y = abs(x), abs(y)
q = deque([(0, 0)]) # Missing import check: 'deque' is from collections
visited = set()
steps = 0
while q:
    # level-by-level BFS
    for _ in range(len(q)):
        cur = q.popleft()
        visited.add(cur) # <--- BUG: Updating visited too late! (Causes TLE)
                         # This should be done when appending to q.
        
        if cur[0] == x and cur[1] == y:
            return steps
            
        for dx, dy in dirs:
            nx, ny = cur[0] + dx, cur[1] + dy
            # same direction
            if nx >= -1 and ny >= -1 and (nx, ny) not in visited:
                q.append((nx, ny))
                # BUG: Node added to queue but not marked as visited.
                # Other nodes in this same level will add (nx, ny) again!
    steps += 1
return -1
```

---

## ⚡ 2. Bidirectional BFS (Optimal)

For large boards, searching from both ends is vastly superior.

### Why it's Faster
Instead of one massive expanding circle ($O(B^d)$), we expand two smaller circles from the start and the target ($O(B^{d/2})$). They meet in the middle, visiting significantly fewer nodes.

### implementation
```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if (x, y) == (0, 0): return 0
        
        dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        q_start, q_end = {(0, 0)}, {(x, y)}
        visited_start, visited_end = {(0, 0): 0}, {(x, y): 0}
        
        while True:
            # Expand the smaller frontier for efficiency
            if len(q_start) > len(q_end):
                q_start, q_end = q_end, q_start
                visited_start, visited_end = visited_end, visited_start
            
            next_q = set()
            for cx, cy in q_start:
                d = visited_start[(cx, cy)]
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in visited_end:
                        return d + 1 + visited_end[(nx, ny)]
                    if (nx, ny) not in visited_start and nx >= -1 and ny >= -1:
                        visited_start[(nx, ny)] = d + 1
                        next_q.add((nx, ny))
            q_start = next_q
```
