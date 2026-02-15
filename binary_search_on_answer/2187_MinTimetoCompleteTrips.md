# LeetCode 2187: Minimum Time to Complete Trips

This problem is a classic example of the **"Binary Search on Answer"** pattern. Below is the full breakdown including the analogy, mental model, and fixed code.

---

## 🏦 The Analogy: The Bank Counters
Imagine there are 3 bank counters with different service speeds: `[2, 5, 3]` minutes per person.
- You are the **5th** person in line (4 people ahead of you).
- You want to know the **earliest time** you can start being served.

**Why is it 3 minutes?**
1.  **t=0**: P1, P2, P3 start at counters A, B, C.
2.  **t=2**: Counter A (speed 2) finishes P1. P4 (the 4th person) immediately takes Counter A.
3.  **t=3**: Counter C (speed 3) finishes P3. Counter C is now free for **YOU** (P5).
4.  **Conclusion**: At 3 minutes, 4 people have been "started" or "assigned", and you can begin.

---

## 🏎️ Mental Model: The Speedometer
We are searching for the **Minimum Time ($T$)**.
- If $T$ is too small (e.g., 1 min), the buses won't finish enough trips.
- If $T$ is too large (e.g., 1,000,000 mins), they finish way more than needed.
- Because the number of trips **increases monotonically** with time, we can use Binary Search to find the exact "threshold" time.

---

## 🐛 Common Pitfalls (Bug Analysis)
When implementing this, watch out for these two common errors:

1.  **Goal Comparison**: In your `check(guess)` function, you must compare the trip count against `totalTrips`, **not** against `guess` (the time).
    *   ❌ `return cnt >= guess`
    *   ✅ `return cnt >= totalTrips`

2.  **Search Boundaries**: Hardcoding `left, right = [5, 15]` will fail for larger inputs.
    *   **Lower bound**: `1` (or `min(time)`).
    *   **Upper bound**: A time that is guaranteed to work, like `min(time) * totalTrips`.

---

## 🛠️ Final Verified Implementation

```python
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def canComplete(guess):
            cnt = 0
            for t in time:
                # How many trips can this bus finish in 'guess' time?
                cnt += guess // t
            return cnt >= totalTrips

        # 1. Define safe search boundaries
        left = 1
        right = min(time) * totalTrips
        ans = right

        # 2. Binary Search for the minimum threshold
        while left <= right:
            mid = left + (right - left) // 2
            if canComplete(mid):
                ans = mid       # This time works, try smaller
                right = mid - 1
            else:
                left = mid + 1  # Not enough trips, need more time
        return ans
```

---

## 🏁 The Search Range: Why `min(time)`?

One of the trickiest parts of Binary Search on Answer is setting the `right` (upper bound). In this problem, we use:
`right = min(time) * totalTrips`

### Why `min` and not `max`?
You might assume that `max(time) * totalTrips` is the safe choice because the slowest bus takes the longest. While that is true, it is **unnecessarily large**.

1.  **The Goal**: We need an upper bound that is **guaranteed** to be able to complete the trips.
2.  **The Logic**: If we only had **one** bus—the fastest one (`min(time)`)—it would complete all `totalTrips` in exactly `min(time) * totalTrips` minutes.
3.  **The Conclusion**: Since adding more buses (the slower ones) can only help finish the trips **faster**, the total time will **never exceed** the time it takes for the fastest bus to do it alone.

**Example**: `time = [2, 5, 10]`, `totalTrips = 10`
*   **Fastest Bus alone**: Takes $2 \times 10 = 20$ minutes. (Guaranteed to work).
*   **Slowest Bus alone**: Takes $10 \times 10 = 100$ minutes. (Also works, but creates a huge search space).
*   Using `min(time)` keeps your search space tight and professional!

---

## 📊 Complexity
- **Time Complexity**: $O(N \log M)$, where $N$ is the number of buses and $M$ is the search range (`min(time) * totalTrips`).
- **Space Complexity**: $O(1)$ extra space.
