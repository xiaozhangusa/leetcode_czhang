# Python Priority Queue: Tuple Comparison & Tie-breakers

In Python, the `heapq` module implements a **min-heap**. When you push a tuple into the heap, Python uses **lexicographical ordering** to determine the priority. This is the key to handling multiple constraints (tie-breakers) easily.

## 1. How Tuple Comparison Works
When comparing two tuples, Python follows these steps:
1. Compare the **first element**.
2. If the first elements are equal, compare the **second element**.
3. If those are equal, compare the **third element**, and so on.

### Example:
```python
(2, 5) < (3, 1)  # True, because 2 < 3
(2, 1) < (2, 5)  # True, because 1 < 5
```

## 2. Default Tie-breakers (Min-Heap)
In a problem like "K Weakest Rows", where you want the smallest value first, and then the smallest index as a tie-breaker, the default behavior works perfectly:

```python
import heapq

min_heap = []
# (value, index)
heapq.heappush(min_heap, (2, 5))
heapq.heappush(min_heap, (2, 1))

print(heapq.heappop(min_heap)) # Output: (2, 1) - Smallest value, then smallest index
```

---

## 3. The Negation Trick (Custom Tie-breakers)
If you want to reverse the priority for a specific element (e.g., **Min** value but **Max** index for tie-breakers), you can negate the value.

### Goal: Smallest value first, but LARGER index if values tie
```python
import heapq

min_heap = []
# (value, -index)
heapq.heappush(min_heap, (2, 5))
heapq.heappush(min_heap, (2, 1))

val, neg_idx = heapq.heappop(min_heap)
print(val, -neg_idx) # Output: 2 5 (Larger index came first)
```
**Why?** Because `-5` is mathematically smaller than `-1`, so the min-heap pops it first.

---

## 4. Summary Table
Use this table to design your tuples based on your sorting needs:

| Requirement | Tuple Structure | Logic |
| :--- | :--- | :--- |
| **Min** Val, **Min** Index | `(val, idx)` | Standard lexicographical order |
| **Min** Val, **Max** Index | `(val, -idx)` | Negate index to flip tie-breaker |
| **Max** Val, **Min** Index | `(-val, idx)` | Negate value to simulate max-heap |
| **Max** Val, **Max** Index | `(-val, -idx)` | Negate both for a true "Max-Max" heap |

> [!TIP]
> Always remember to "re-negate" the value or use `abs()` when popping from the heap if you need the original value back.
