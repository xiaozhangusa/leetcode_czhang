# Binary Search: The "Adjacent Convergence" Template

When searching for a boundary (like the maximum valid length or the first index that satisfies a condition), the `lo + 1 < hi` template is often the most robust and "stress-free" choice.

## 1. The Template Logic

```python
lo = initial_known_valid    # Value you are SURE is True
hi = initial_known_invalid  # Value you are SURE is False (often boundary + 1)

while lo + 1 < hi:          # Search as long as there is an integer between them
    mid = lo + (hi - lo) // 2
    
    if condition(mid):      # If mid is valid
        lo = mid            # Shrink toward high, keep mid as 'last known valid'
    else:                   # If mid is invalid
        hi = mid            # Shrink toward low, keep mid as 'ceiling'

# Result is usually 'lo' for maximum valid, 'hi' for minimum invalid.
return lo
```

## 2. Why use `lo + 1 < hi`?

| Feature | Logic |
| :--- | :--- |
| **No Infinite Loops** | The loop stops when `lo` and `hi` are adjacent ($4$ and $5$). $4+1$ is not less than $5$, so it terminates. |
| **No `+1` / `-1` Confusion** | You don't need `lo = mid + 1`. You simply set the boundary to `mid`. |
| **Clear Invariants** | `lo` always points to a valid state; `hi` always points to an invalid state. |
| **Overflow Safe** | `lo + (hi - lo) // 2` is safer than `(lo + hi) // 2` in languages with fixed-size integers. |

## 3. Comparison of Common Templates

| Template | Terminating Condition | Boundary Update | Best For |
| :--- | :--- | :--- | :--- |
| **`while lo <= hi`** | `lo > hi` | `lo = mid + 1`, `hi = mid - 1` | Finding a specific value (exact match). |
| **`while lo < hi`** | `lo == hi` | Requires careful `+1` on `mid` or `lo` | Finding a boundary where you want to stop *on* the answer. |
| **`while lo + 1 < hi`** | `lo + 1 == hi` | Simple `lo = mid`, `hi = mid` | **Boundary Finding (Max/Min valid)**. Most robust for interviews. |

## 4. Pro-Tip: Floating Point Search
If you are searching for a continuous decimal value (like `sqrt(x)`), the logic is identical but the termination condition changes to a precision threshold:

```python
while hi - lo > 1e-7:
    mid = (lo + hi) / 2
    if mid * mid < x: lo = mid
    else: hi = mid
```
