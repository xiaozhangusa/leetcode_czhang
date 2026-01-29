# Counting Bits: Detailed Explanation of the DP Solution

This document explains the $O(n)$ Dynamic Programming approach for calculating the number of set bits (1s) for all integers from $0$ to $n$.

## The Core Logic

The solution relies on one fundamental bitwise identity:

> **The number of set bits in $x$ is equal to the number of set bits in $(x \ \& \ (x - 1))$ plus one.**

---

### Phase 1: What is `x & (x - 1)`?

Perform a bitwise `AND` between a number and the number immediately before it. This operation always **flips the rightmost `1` to a `0`**.

#### Example: $x = 6$
1.  **Binary of $x$ (6)**: `1 1 0`
2.  **Binary of $x-1$ (5)**: `1 0 1`
3.  **Result of `6 & 5`**:
    ```text
       1 1 0  (6)
     & 1 0 1  (5)
     -------
       1 0 0  (4)
    ```
Notice that `4` is exactly `6` but with that last `1` removed.

---

### Phase 2: Why the `+ 1`?

Think of it like a subtraction problem for bits:
1.  If $y = x \ \& \ (x - 1)$, we know that $y$ is just $x$ with one less "set bit" (one less `1`).
2.  Therefore, to get the count of `1`s in $x$, we take the count of `1`s in $y$ and **add that one bit back**.

**In formula terms:**
$$\text{SetBits}(x) = \text{SetBits}(x \ \& \ (x - 1)) + 1$$

---

### Phase 3: The DP Connection

In Dynamic Programming, we solve small problems and use them to solve larger ones. 

1.  We know that `x & (x - 1)` is **always smaller** than `x`.
2.  So, by the time our loop reaches `x`, we have **already calculated** the result for `x & (x - 1)`.
3.  We just look up that previous answer and add `1`.

#### Visual Trace ($n = 6$)

| $x$ | Binary | $y = x \ \& \ (x-1)$ | `ans[y]` (Previously found) | `ans[x] = ans[y] + 1` |
|:---:|:---:|:---:|:---:|:---:|
| **0** | `000` | — | — | **0** (Base Case) |
| **1** | `001` | `0` | `ans[0] = 0` | `0 + 1 = 1` |
| **2** | `010` | `0` | `ans[0] = 0` | `0 + 1 = 1` |
| **3** | `011` | `2` | `ans[2] = 1` | `1 + 1 = 2` |
| **4** | `100` | `0` | `ans[0] = 0` | `0 + 1 = 1` |
| **5** | `101` | `4` | `ans[4] = 1` | `1 + 1 = 2` |
| **6** | `110` | `4` | `ans[4] = 1` | `1 + 1 = 2` |

---

### Summary of Benefits
- **Speed**: $O(n)$ because we only look at each number once.
- **Space**: $O(1)$ extra space (since we only use the output array).
- **Simplicity**: No complex bit manipulation or built-in functions required.
