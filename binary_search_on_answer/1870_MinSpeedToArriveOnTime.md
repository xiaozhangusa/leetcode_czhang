# LeetCode 1870: Minimum Speed to Arrive on Time

This problem is a deceptive "Binary Search on Answer" problem that introduces two critical challenges: **Wait Time Logic** and **Integer vs Floating-Point Precision**.

---

## 🚂 The Scheduling Logic: The Last Train Exception
In this problem, you travel through $N$ trains.
- **Trains 1 to $N-1$**: Each train ride finishes, but you can only depart for the next one at an **integer hour**. 
    - Logic: `total_time += math.ceil(dist[i] / speed)`
- **The Last Train ($N$)**: Once you arrive at your office, you don't need to wait for a "next train". You just care if you are under the deadline.
    - Logic: `total_time += dist[-1] / speed` (No rounding!)

---

## ⚡ The TLE Trap: Integer vs Float Binary Search
The problem asks for the **"minimum positive integer speed"**. 

1.  **Why Float Binary Search fails**: 
    - Using `while left < right` with floats can lead to precision issues and **infinite loops** or extremely long execution times (TLE).
    - Even if it finishes, you'd have to use `math.ceil(ans)` at the end, which is less reliable.
2.  **The Solution**: Treat the possible **speeds** as an array of integers `[1, 2, 3, ..., 10^7]`.
    - `left, right = 1, 10**7`
    - `mid = (left + right) // 2`
## 🏁 Boundary Selection: Why `1` and `10^7`?

Choosing the search range for this problem requires looking at the **constraints** and the **decimal precision**.

1.  **`left = 1`**: The problem asks for the minimum **positive integer** speed. $1$ is the smallest possible answer.
2.  **`right = 10**7`**: This is the "magic number" for this problem.
    *   **The Constraint**: The problem description explicitly states: *"Tests are generated such that the answer will not exceed 10^7."*
    *   **The Math**: `hour` has up to **2 decimal places**. If you have $N$ trains and $hour = (N-1) + 0.01$, you have only **0.01 hours** to finish the last train. If the last train's distance is $10^5$, the required speed is $10^5 / 0.01 = 10,000,000$ ($10^7$).

---

## �️ Interview Tip: Why `left = 1` and not something complex?

You might be tempted to calculate a more "intelligent" lower bound, like `sum(dist) / total_hours` or `sum(dist) / len(dist)`. Here is why you should **stick to 1**:

1.  **Dimensional Mismatch**: `sum(dist) / len(dist)` calculates the *average distance* per train, which has the wrong units (km vs km/h) and doesn't account for time or wait logic.
2.  **Safety First**: Complex formulas are easy to get wrong under interview pressure. If your `left` is accidentally higher than the real answer, you will fail. `left = 1` is **impossible to get wrong**.
3.  **Efficiency**: Binary Search is $O(\log N)$. Searching from `1` to $10^7$ takes about 23 steps. Even if you start from a perfectly optimized `left = 100`, you only save 6-7 steps. The risk of being wrong far outweighs the negligible performance gain.

---

## 🛠️ Final Verified Implementation

```python
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def canArrive(speed):
            # speed is an integer
            time_spent = 0
            # Round up for all trips except the very last one
            for i in range(len(dist) - 1):
                time_spent += math.ceil(dist[i] / speed)
            
            # Last trip does not require waiting
            time_spent += dist[-1] / speed
            return time_spent <= hour

        # Constraints say answer won't exceed 10^7
        left, right = 1, 10**7
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canArrive(mid):
                ans = mid       # Found a valid speed, try smaller
                right = mid - 1
            else:
                left = mid + 1  # Too slow, need more speed
                
        return ans
```

---

## 💡 Key Takeaway
If a problem asks for an **Integer** answer, always use **Integer Binary Search**. It's faster, safer, and avoids rounding errors.
