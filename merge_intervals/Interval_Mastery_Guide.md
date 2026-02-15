# 🛠️ Interval Problem Mastery Guide

Interval problems are a classic "Greedy + Sorting" cluster. Mastering them requires a clear mental model and a few reusable templates.

---

## 🏛️ Level 1: Foundations

### 🧠 Mental Model: The "Timeline Tape"
Imagine a long strip of **magnetic tape** representing time or distance.
- **Intervals** are pieces of colored tape you stick onto the strip.
- **The Question** usually boils down to:
    - How much total space is covered? (Union)
    - Where do they double up? (Overlap/Intersection)
    - Where are the empty spots? (Gaps)

### 🎯 The Core Greedy Choice: Start vs. End Time
The most common mistake is sorting by the wrong boundary. 
- **Sort by Start Time** (The Relay Race): Use when you need to see how far you can stretch "coverage" (Merge, Gaps, Union).
- **Sort by End Time** (The Tetris Packing): Use when you want to pack the maximum number of *non-overlapping* tasks (Scheduling).

---

## 🍞 Level 2: Bread & Butter Patterns

### 1. The "Sort & Merge" (Union)
Used to combine overlapping intervals into a single range.
- **Representative Problem**: [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- **Mental Model**: Squeezing overlapping sponges into one.

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0]) # Start Time!
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```

### 2. The "Rolling Gap" (Capped Sum)
Used when a duration is "reset" by the next event. Instead of merging intervals, we calculate the contribution of each event on-the-fly.
- **Representative Problem**: [495. Teemo Attacking](https://leetcode.com/problems/teemo-attacking/)
- **Mental Model**: The **"Refillable Water Bottle"**. You start drinking (poison), but if someone refills your bottle (new attack) before it's empty, you don't drink "more" total water than the capacity—you just reset the timer.

#### 📊 Visualization (O(1) Space Logic)
Imagine attacks at `[1, 2]` with `duration = 2`:
```text
Time:    1   2   3   4
Attack:  A1  A2
A1 Poison: [---] (1 to 3)
A2 Poison:     [---] (2 to 4)
-------------------------
Total:     [=======] (1 to 4) = 3 seconds
```
**The Math**:
- Gap between A1 and A2 is `2 - 1 = 1`. 
- Since `Gap (1) < Duration (2)`, A1 only contributes **1 second** of unique poison.
- The **last attack** always contributes the **full duration**.
- **Total** = $\sum \min(\text{duration}, \text{next\_start} - \text{curr\_start}) + \text{duration}$.

> [!NOTE]
> ### ⏰ The "Countdown Alarm" Mental Model
> The core of understanding this is: **Poison duration is interrupted by the "next attack".**
> 
> Imagine the poison is a **10-minute countdown alarm**. Every time Teemo attacks, he forcibly **resets** the alarm to 10:00 and starts the countdown again.
> 
> 1.  **Attack 1 (t=1):** Alarm starts counting from 10:00.
> 2.  **Attack 2 (t=5):** At this point, the alarm has reached 6:00. Teemo hits you, **BANG**, the alarm is reset back to 10:00.
>     - **Result**: Attack 1 only ran for **4 minutes** before being interrupted.
> 3.  **... Last Attack (t=100):** Teemo hits you and disappears.
>     - **Result**: The alarm resets to 10:00, but because **no one else comes to interrupt it**, it runs its full **10-minute course** until it hits zero.
> 
> #### 📊 Visual Comparison
> Assume `duration = 10`, attacks at `[1, 5, 20]`:
> - **t=1 attack**: 4s gap until next attack $\rightarrow$ contributes **4s**.
> - **t=5 attack**: 15s gap until next attack $\rightarrow$ gap is long, but poison only lasts 10s $\rightarrow$ contributes **10s**.
> - **t=20 attack (last)**: The "End of Time" follows $\rightarrow$ inevitably runs for **10s**.
>   - **Total**: $4 + 10 + 10 = 24$ seconds.
> 
> **The Essence**: This $O(1)$ space algorithm works because: "Everyone looks at the person behind them to see how much time they have left; but the last person only looks at themselves."

```python
def find_poisoned_duration(timeSeries, duration):
    if not timeSeries: return 0
    total = 0
    for i in range(len(timeSeries) - 1):
        # Only add the "unique" time before the next reset
        total += min(duration, timeSeries[i+1] - timeSeries[i])
    return total + duration # Always add the full last duration
```
- **Optimization**: $O(1)$ Space! No need to store intervals.

#### 👯 Direct Cousins (Related Problems)
The "Rolling Gap" logic isn't just for intervals; it's a powerful way to handle **cumulative contribution** based on neighbors:

1.  **[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)**: Instead of findining complicated intervals to buy/sell, just sum every positive "gap" between today and tomorrow: `res += max(0, prices[i+1] - prices[i])`.
2.  **[135. Candy](https://leetcode.com/problems/candy/)**: You compare a child to their neighbor and adjust their "candy level" based on the gap in ratings.
3.  **[853. Car Fleet](https://leetcode.com/problems/car-fleet/)**: A **Greedy** approach using "Rolling Gap" in **Arrival Times**. If Car B behind takes less time than Car A in front, the arrival time gap "closes" before the target, forcing a merge.

---

## 🌊 Level 3: Advanced Flow Techniques

### 3. The "Sweep Line" (Scanner)
Treat starts as `+1` events and ends as `-1` events. Sort and sweep left-to-right.
- **Representative Problem**: [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- **Mental Model**: A scanner counting how many signals are currently active.

```python
def sweep_line(intervals):
    events = sorted([(s, 1) for s, e in intervals] + [(e, -1) for s, e in intervals])
    active, max_active = 0, 0
    for time, val in events:
        active += val
        max_active = max(max_active, active)
    return max_active
```

### 4. Difference Array (Batch Cleanup)
Use when you have a fixed range and many updates before one final query.
- **Representative Problem**: [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)
- **Strategy**: `arr[start] += val`, `arr[end + 1] -= val`.

### 5. Two-Pointer (The Zipline)
Comparing two sorted lists to find overlaps. 
- **Representative Problem**: [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- **Key**: Advance the pointer of the interval that ends first.

---

## 🏗️ Level 4: Heavy Machinery (Advanced DS)

### 6. Segment Tree (The Management Hierarchy)
The boss of **online** range updates and queries.
- **Representative Problems**: [307. Range Sum Query](https://leetcode.com/problems/range-sum-query-mutable/), [699. Falling Squares](https://leetcode.com/problems/falling-squares/)
- **Mental Model**: CEO delegating tasks to divisional managers down to line workers.

### 7. SortedList (The Living Calendar)
Maintaining a set of non-overlapping intervals dynamically.
- **Use Case**: Inserting intervals while preventing double-booking (Binary search on neighbors).

---

## 🚀 Level 5: Problem Discovery Toolkit

| Keyword | Goal | Best strategy |
| :--- | :--- | :--- |
| **Merge** | Combine all overlaps | Sort by **Start Time** |
| **Scheduling** | Max number of tasks | Sort by **End Time** |
| **Intersection** | Where lists meet | **Two Pointers** |
| **Gaps** | Find the "holes" | Compare `current.start` vs `prev.end` |
| **Room/Peak** | Max overlaps at once | **Sweep Line** or Heap |
| **Dynamic** | Update & Query often | **Segment Tree** |

---

> [!TIP]
> **Pro Tip**: If the question asks for the **minimum** count to cover a range, think **Greedy** (sort by start, pick the one extending furthest). If it asks for the **maximum** count of non-overlapping items, sort by **end time**.
