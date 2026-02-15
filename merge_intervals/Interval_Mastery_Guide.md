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

### 2. The "Rolling Reset" (Capped Sum)
Used when a duration is "reset" by the next event.
- **Representative Problem**: [495. Teemo Attacking](https://leetcode.com/problems/teemo-attacking/)
- **Strategy**: Simply add `min(duration, next_start - current_start)`.

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
