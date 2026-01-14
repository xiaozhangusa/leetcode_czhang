# Deep Dive: Binary Search & Sliding Window (LeetCode 340)

This document explains the "Robust Binary Search" approach for finding the longest substring with at most $K$ distinct characters.

---

## 1. The Core Strategy: "Length Hunting"

Instead of searching for indices, we are searching for the **maximum valid length**.
*   If a substring of length $L$ is valid, then any $L$ smaller than it *might* be the maximum.
*   If a length $L$ is invalid, anything larger than it is definitely invalid.

This "monotonic" property (True, True, True, False, False) makes it a perfect candidate for Binary Search.

---

## 2. The Transparent Template: `while lo + 1 < hi`

This is the "stress-free" template that prevents infinite loops and off-by-one errors.

```python
lo, hi = 0, len(s) + 1
while lo + 1 < hi:
    mid = lo + (hi - lo) // 2
    if self.isValid(s, mid, k):
        lo = mid
    else:
        hi = mid
return lo
```

### Why `hi = len(s) + 1`? (The Explorer Analogy)
Think of an explorer building a bridge across a canyon.
*   **`lo` (Safe Spot):** The last plank you know is solid (0 planks is always valid).
*   **`hi` (Danger marker):** A point in the fog you are CERTAIN is empty air.
*   **The "No-Fly Zone":** Binary search treats `hi` like a wall it can never touch. If your string length is 5, and you set `hi = 5`, you are telling the computer: *"I am 100% sure the bridge can't reach Plank 5."* 
*   Because of this, the bridge will only ever test up to Plank 4. By setting `hi = 6`, you allow the "Explorer" (`mid`) to actually step on Plank 5 to see if it holds.

**Rule of thumb:** `hi` should be the smallest value you are **certain** is impossible. For a string of length $N$, a substring of $N+1$ is physically impossible.

---

## 3. The `isValid` Helper: Fixed-Size Sliding Window

When binary search asks "Is length $L$ possible?", we use a sliding window of **exactly size $L$** to scan the string.

### Correct Window Math
The most common bug is the window size calculation.
*   **Indices:** `start` and `end`.
*   **Formula:** `Length = end - start + 1`.
*   **Example:** If `start = 0` and `end = 2`, the characters are at $0, 1, 2$. Total length is $2 - 0 + 1 = 3$.

### Implementation Pattern
```python
def isValid(self, s: str, sublen: int, k: int) -> bool:
    if sublen == 0: return True
    freq = {}
    start = 0
    for end in range(len(s)):
        # 1. Add new character
        freq[s[end]] = freq.get(s[end], 0) + 1
        
        # 2. Maintain window size: Shrink if it gets too big
        if end - start + 1 > sublen:
            freq[s[start]] -= 1
            if freq[s[start]] == 0: del freq[s[start]]
            start += 1
        
        # 3. Check validity: Only when we have reached the target sublen
        if end - start + 1 == sublen:
            if len(freq) <= k:
                return True
    return False
```

---

## 4. Key Takeaways

1.  **Safety First:** `lo + 1 < hi` is more robust than `lo <= hi` for finding boundaries because it removes the need for `mid + 1` and `mid - 1`.
2.  **Boundary Truth:** Set `lo` to a known valid (0) and `hi` to a known invalid (`len+1`).
3.  **Quantity vs Index:** When searching for a quantity (length), your `lo` and `hi` should reflect that quantity directly.
4.  **Window Precision:** Always remember `end - start + 1` to avoid off-by-one errors.
