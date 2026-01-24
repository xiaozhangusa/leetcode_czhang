# Understanding the K-th Largest Element Problem

This document summarizes the core logic and properties of the `KthLargest` stream implementation using a **Min-Heap**.

## 1. The Strategy: The "Elite Club" Analogy
To find the **k-th largest** element in a stream, we only care about the **Top k** values seen so far. We ignore everything else.

- **The Club**: We maintain a min-heap with a maximum capacity of `k`.
- **The Bouncer (Min-Heap)**: A min-heap always keeps its **smallest** element at the root (`heap[0]`). 
- **The Ranking**: In a club of the `k` largest people, the **weakest** person (the minimum) is exactly the **k-th largest** person overall.

## 2. Code Implementation Logic

```python
def add(self, val: int) -> int:
    heapq.heappush(self.heap, val)    # 1. New member enters the club
    if len(self.heap) > self.k:      # 2. Club is over capacity (> k)
        heapq.heappop(self.heap)     # 3. Kick out the weakest member
    return self.heap[0]              # 4. The weakest member left is the k-th largest
```

### Why this handles everything:
- **Heap Growth**: If the heap has fewer than `k` elements, the `if` condition fails, and no one is popped. The heap naturally grows until it reaches size `k`.
- **Finding the Max**: The **1st largest** element is guaranteed to be in the heap (since it's part of the top $k$), but it will be somewhere in the "leaves" of the tree, not at the root.

## 3. Important Heap Properties

### Lexicographical Comparison (Tuples)
If you store tuples in a heap (e.g., `(score, index)`), `heapq` compares the first element first. To simulate a max-heap using `heapq`, we often use negative values: `(-score, index)`.

### Memory Structure vs. Logical Structure
A heap in Python is a flat list, but it represents a binary tree where `parent <= children`.
- **Example**: `[10, 20, 5, 30, 15]` becomes `[5, 15, 10, 30, 20]` after `heapify()`.
- **`heap[0]`**: Guaranteed to be the smallest.
- **`heap[-1]`**: **Not** guaranteed to be the largest (it's just the last leaf).

## 4. Constraint Awareness
The problem guarantees `1 <= k <= nums.length + 1`. 
This ensures that by the time you need to return a value from `add()`, your "Elite Club" will have at least `k` members (or will be exactly at `k` members), making the result at `heap[0]` valid.

---
*Created for LeetCode 703: Kth Largest Element in a Stream*
