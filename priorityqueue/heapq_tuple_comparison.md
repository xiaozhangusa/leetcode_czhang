# Python `heapq` and Tuple Comparison

In Python, the `heapq` module implements a **min-heap** where the smallest element is always at the root. When you push a tuple into a heap, the comparison behavior is determined by Python's standard tuple comparison rules.

## 1. Lexicographical Comparison
Python compares tuples element by element, starting from the first index (index 0).

- **Step 1:** Compare `tuple1[0]` and `tuple2[0]`. If they are different, the result of this comparison determines the order.
- **Step 2:** If `tuple1[0] == tuple2[0]`, then compare `tuple1[1]` and `tuple2[1]`.
- **Step 3:** This continues until a difference is found or all elements are compared.

## 2. `(-s, idx)` vs `(idx, -s)`

The order of elements in the tuple changes what the heap is actually "sorting" by.

### `(-s, idx)` — Sort by Score (Decreasing)
This is used in `506_RelativeRanks.py` to simulate a **max-heap** for scores.

- **Primary Sort Key:** `-s` (Negative Score). 
- **Secondary Sort Key:** `idx` (Original Index).
- **Behavior:** The heap identifies the "smallest" negative score (which is the **largest** positive score) and keeps it at the top.
- **Example:**
  - Tuple A: `(-10, 1)` (Score 10 at Index 1)
  - Tuple B: `(-5, 0)` (Score 5 at Index 0)
  - Result: `(-10, 1)` is "smaller" than `(-5, 0)` because `-10 < -5`. It will be popped first.

### `(idx, -s)` — Sort by Index
This would **not** work for the Relative Ranks problem.

- **Primary Sort Key:** `idx` (Original Index).
- **Secondary Sort Key:** `-s` (Negative Score).
- **Behavior:** The heap identifies the "smallest" index and keeps it at the top, regardless of what the score is.
- **Example:**
  - Tuple A: `(0, -5)` (Index 0 with Score 5)
  - Tuple B: `(1, -10)` (Index 1 with Score 10)
  - Result: `(0, -5)` is "smaller" than `(1, -10)` because `0 < 1`. It will be popped first, even though it has a lower score.

## Summary Table

| Representation | Top Priority | Tie-Breaker | Use Case |
| :--- | :--- | :--- | :--- |
| `(-s, idx)` | Score (Highest first) | Index (Lowest first) | Finding the highest scores first (medals). |
| `(idx, -s)` | Index (First occurrence) | Score (Highest first) | Processing items in original order, but sorting by score if indices match. |
