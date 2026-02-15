# LeetCode 2226: Maximum Candies Allocated to K Children

This problem uses the **"Binary Search on Answer"** pattern to find the maximum possible candy allocation that satisfies the given condition.

---

## 🏎️ Mental Model: The Candy Distributor
We are searching for the **Maximum Number of Candies ($X$)** each child gets.
- If $X$ is small (e.g., 1 candy), we can definitely give it to `k` children (if total candies >= `k`).
- If $X$ is very large (e.g., `max(candies)`), we might not have enough piles to satisfy `k` children.
- As $X$ increases, the number of successful allocations **decreases monotonically**. This is the perfect signal for Binary Search.

---

## 🐛 Bug Analysis: The ZeroDivisionError
When implementing this, a very common pitfall is the **Zero Division** bug.

### The Cause
*   If you set `left = 0`, the binary search `mid` can become `0`.
*   Inside your `check(guess)` function: `cnt += pile // guess`.
*   When `guess` is `0`, Python Throws a `ZeroDivisionError`.

### The Fix
1.  **Start from 1**: Set `left = 1`. This is the smallest "meaningful" answer we are searching for.
2.  **Handle the 0 Case**: Initialize `ans = 0`. If the binary search fails to find any valid allocation for $X \ge 1$, the function will naturally return the initial `0`.

---

## 🛠️ Final Verified Implementation

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canAllocate(guess):
            # How many children can we satisfy if each gets 'guess' candies?
            cnt = 0
            for c in candies:
                cnt += c // guess
            return cnt >= k

        # 1. Start search from 1 to avoid ZeroDivisionError
        # 2. ans = 0 handles the case where k children cannot even get 1 candy
        left, right = 1, max(candies)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if canAllocate(mid):
                ans = mid       # This works, try to give even more
                left = mid + 1
            else:
                right = mid - 1 # Too many candies, shrink the guess
        return ans
```

---

## 📊 Complexity
- **Time Complexity**: $O(N \log M)$, where $N$ is the number of candy piles and $M$ is the maximum pile size.
- **Space Complexity**: $O(1)$ extra space.
