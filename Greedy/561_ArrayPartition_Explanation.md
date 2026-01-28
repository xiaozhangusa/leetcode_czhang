# LeetCode 561: Array Partition I - Mathematical Proof & Explanation

This document explains why the greedy strategy for the Array Partition problem is mathematically optimal and how the optimized Python implementation works.

## 1. Greedy Strategy
The optimal strategy is:
1.  **Sort** the array: $x_1 \le x_2 \le \dots \le x_{2n}$
2.  **Pair** adjacent elements: $(x_1, x_2), (x_3, x_4), \dots, (x_{2n-1}, x_{2n})$
3.  **Sum** the minimum of each pair: $x_1 + x_3 + \dots + x_{2n-1}$

---

## 2. Mathematical Proof (Exchange Argument)

Suppose we have an optimal pairing $P$ that pairs elements non-adjacently.

### Smallest Element Logic
Consider $x_1$. In any pairing, $\min(x_1, x_k) = x_1$ because $x_1$ is the global minimum. To maximize the total sum, we want to pair $x_1$ with the smallest possible partner ($x_2$) to avoid "wasting" a larger number $x_k$ that could contribute more to the sum in a different pair.

### The Exchange
If $x_1$ is paired with $x_k$ ($k > 2$) and $x_2$ is paired with $x_j$ ($j > 2$):
*   **Current Sum contribution:** $x_1 + \min(x_2, x_j)$
*   **Swapped Sum contribution:** $x_1 + \min(x_k, x_j)$

Since $x_k \ge x_2$, the swapped sum ($C_{P'}$) is guaranteed to be $\ge$ the original sum ($C_P$). Thus, pairing $(x_1, x_2)$ is always optimal.

---

## 3. Python Optimization (`sum(nums[::2])`)

The optimized implementation `return sum(nums[::2])` is faster than `pop(0)` because it avoids $O(n)$ element shifting and executes mostly in high-speed C code.

### Breakdown of `nums[::2]`
This uses **extended slicing** `[start:stop:step]`.

*   **Logic**: It calculates indices using $index = 0 + (i \times 2)$.
*   **Stride**: It "steps over" every other element in a single pass.
*   **Example Trace**:
    *   **Input**: `[6, 2, 6, 5, 1, 2]`
    *   **Sorted**: `[1, 2, 2, 5, 6, 6]`
    *   **Slice `[::2]`**:
        *   Index 0: **1** (Pick)
        *   Index 1: 2 (Skip)
        *   Index 2: **2** (Pick)
        *   Index 3: 5 (Skip)
        *   Index 4: **6** (Pick)
        *   Index 5: 6 (Skip)
    *   **Result**: `[1, 2, 6]` $\rightarrow$ `sum` = **9**

### Performance Insight
| Method | Complexity | Why? |
| :--- | :--- | :--- |
| `pop(0)` | $O(n^2)$ | Each `pop(0)` shifts all remaining $O(n)$ elements. |
| `nums[::2]` | $O(n \log n)$ | Dominated by sorting. The slicing/summing is $O(n)$ and runs in optimized C code. |

> [!TIP]
> `nums[::2]` creates a temporary list. For extremely large datasets where memory is tight, you can use `itertools.islice(nums, 0, None, 2)` to sum without making a copy.
