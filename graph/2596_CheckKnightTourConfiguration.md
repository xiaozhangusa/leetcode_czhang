# 🏇 2596. Check Knight Tour Configuration

## Problem Analysis
We are given a grid showing the order of a knight's move. We need to verify if every single move follows the knight's "L" shape and if the tour starts at the correct position.

---

## 🧠 The Mental Model: The "Invisible Fence"

The most common error in grid problems is the `IndexError: list index out of range`. 

### The Playground vs. The Open Field
- **In 1197 (Min Knight Moves)**: The board was infinite. The knight could jump anywhere.
- **In 2596 (Knight Tour)**: The board is an $n \times n$ playground with a physical fence.

If you ask your code to check `grid[nx][ny]` **before** checking if `nx, ny` are within `[0, n-1]`, your knight effectively "jumps off the world" and the program crashes. You must always check the "Fence" first:

```python
# 🧱 The Invisible Fence
if 0 <= nx < n and 0 <= ny < n:
    # Now it is safe to check the grid value
    if grid[nx][ny] == next_expected_move:
        ...
```

---

## ⚠️ Common Python Pitfalls

### 1. The Visited Set Trap
In Python, `set((0, 0))` is interpreted as `set( iteration_of_0_0 )`. This creates a set `{0}`, which is completely wrong for tracking coordinates.
- **Wrong**: `visited = set((0, 0))` -> `{0}`
- **Right**: `visited = {(0, 0)}` or `set([(0, 0)])`

#### 🧠 Mastery Insight: Why is `visited` actually redundant here?
In the 1197 (Min Knight Moves) problem, we **needed** a `visited` set to avoid searching the same square forever. But in this problem:
- The grid contains **unique** numbers from `0` to `n*n - 1`.
- We are searching for these numbers in a **strict sequential order** (`0 -> 1 -> 2 ...`).
- Because each number only appears once, the moment we find `move 5`, we know we haven't visited that specific square before (since moved 0-4 are at different squares). The sequence itself prevents us from ever "re-visiting" an old move.

### 2. The XOR Trap (`^` vs `**`)
In many languages (like Java/C++), `^` often implies power in casual conversation, but in Python:
- `^` is **Bitwise XOR**.
- `**` is **Power**.

#### 🧠 Mastery Insight: Why `visited_count == n * n`?
Strictly speaking, if your `for move in range(1, n * n)` loop completes without returning `False`, it means you successfully jumped from `0` all the way to `n*n - 1`.
- Since there are $n \times n$ total squares and you found every move number in a valid knight sequence, you have implicitly visited all $n \times n$ squares exactly once.
- **Conclusion**: `return True` at the end of the loop is technically identical to checking the count, but `visited_count == n * n` is a very common "sanity check" used in interview settings to prove the completeness of the tour.

### 3. The "Finishing Line" Bug (Termination)
In a 5x5 grid, the final move is indexed as **24**. 
- **The Pitfall**: A common error is to successfully reach move 24, but then try to search for "move 25". Since 25 doesn't exist, the code returns `False` at the very last second.
- **The Fix**: Stop the search or return `True` the moment you arrive at `n*n - 1`.

### 4. The "Starting Block" Bug
The problem rules state the knight **must** start at (0,0) at step 0. 
- **The Pitfall**: Forgetting this check will let a valid "shape" tour pass even if it starts on the wrong square.
- **The Fix**: Always check `if grid[0][0] != 0: return False`.

---

## 🥊 Implementation Comparison

| Feature | Your Version (BFS-Style) | My Version (Sequential Simulation) |
| :--- | :--- | :--- |
| **Logic** | Uses `deque` and `visited` set. | Uses simple variables (`cx, cy`). |
| **Efficiency** | Same time complexity, but slightly higher memory for `deque` and `set`. | Minimal memory usage. |
| **Why BFS is Overkill** | BFS is for **unpredictable** paths with many branches. | Sequential tours are **deterministic** (only one "next" square). |
| **Termination** | Often fails at the end by looking for "next move" after total count. | Terminates cleanly at `move == n*n - 1`. |

### Your Corrected BFS-Style Logic
```python
while q:
    cx, cy = q.popleft()
    if moves == n * n - 1: return True # <--- Crucial Termination
    
    found = False
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == moves + 1:
                q.append((nx, ny)) # No visited needed as discussed
                found = True
                break
    if not found: return False
    moves += 1
```

### The Optimized Simulation Logic
```python
# Starting position
cx, cy = 0, 0

# We just jump from number to number in the grid
for move in range(1, n * n):
    found = False
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == move:
            cx, cy = nx, ny
            found = True
            break
    if not found: return False
return True
```

---

## ✅ Final Verified Solution
```python
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
            
        n = len(grid)
        dirs = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        cx, cy = 0, 0
        
        for move in range(1, n * n):
            found = False
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == move:
                    cx, cy = nx, ny
                    found = True
                    break
            if not found: return False
        return True 
```
