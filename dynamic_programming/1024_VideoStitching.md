The problem asks for the **minimum** number of clips to cover the interval $[0, \text{time}]$. This is a classic "Interval Coverage" problem.

## 🧱 Stripped Down: What is this really asking?

If we remove the "video" and "stitching" decoration, the core problem is:
> Given a collection of **intervals** $[start_i, end_i]$, what is the **minimum number of intervals** required to form a continuous union that covers the entire range $[0, T]$?

## 🧠 The Mental Model: "Leap-frogging for Continuity"

- **The Objective**: Connect point $A$ to point $B$ using the fewest possible "bridges."
- **The Constraint**: Each bridge must overlap with the previous one (or the start point). You cannot "jump" over a gap.
- **The Strategy**: At every point you reach, you are looking for the candidate that offers the **furthest leap forward**. You don't care about where the candidate *starts* (as long as it's within your reach), you only care about where it *ends*.

---

## Approach 1: Greedy (The "Jump Game II" Pattern)

This is the most efficient approach. We can transform this problem into **Jump Game II**.

### The Logic
1.  **Preprocessing**: For each possible start time $i$, find the maximum end time $j$ among all clips that start at or before $i$.
2.  **Greedy Strategy**:
    - At any point `current_end`, we look at all clips that start within our current covered range $[0, \text{current\_end}]$.
    - We pick the clip that extends our reach the furthest (`next_end`).
    - If at any point we can't move forward (`next_end == current_end`), and we haven't reached `time`, it's impossible.

### Vivid Example: The Relay Race 🏃‍♂️
Imagine you are organizing a relay race from point 0 to point 10. You have several runners (clips), each can only run a specific section.

**Runners (Clips):** `[[0, 4], [2, 8], [1, 5], [7, 10]]`, **Goal:** `10`

1.  **Start (Point 0):** You look at all runners who can start at 0. Only `[0, 4]` is available.
    - *Decision:* Pick `[0, 4]`. Now you are at point 4. (**Count = 1**)
2.  **At Point 4:** You need someone to take the baton. You look at all runners who can start *before* or *at* 4 (`[2, 8]` and `[1, 5]`).
    - *Decision:* `[2, 8]` goes further than `[1, 5]`. Pick `[2, 8]`. Now you are at point 8. (**Count = 2**)
3.  **At Point 8:** You look for runners starting at or before 8. `[7, 10]` is available.
    - *Decision:* Pick `[7, 10]`. Now you are at point 10. (**Count = 3**)
4.  **Goal Reached!** Result: 3.

---

## Approach 2: Dynamic Programming

Define `dp[i]` as the minimum number of clips required to cover the interval $[0, i]$.

### The Logic
1.  Initialize `dp[0] = 0` and `dp[i] = \infty` for $i > 0$.
2.  For each clip `[start, end]`:
    - For any $j$ from `start + 1` to `end`, we can potentially update `dp[j]`:
      `dp[j] = min(dp[j], dp[start] + 1)`

### Complexity
- **Time**: $O(N \cdot T)$
- **Space**: $O(T)$

---

---

## Intuition Deep Dive: The "Why" behind the Ideas

### Why Greedy works? (The "Greedy Choice" Property)
The intuition is **Maximum Utility**.
Imagine you are at `current_end`. You know you must pick *at least one* more clip to move further. If you have several clips that start before your current position, which one is objectively better?
- A clip that ends at `current_end + 2`?
- Or a clip that ends at `current_end + 10`?

Since both start at a valid time (before you ran out of video), the one that reaches further is **always** better (or at least as good) because it covers everything the shorter clip covers and more. By picking the furthest one, you "buy" yourself the most time before you have to pick another clip, thus minimizing the total count.

### Why DP works? (The "Optimal Substructure")
The intuition is **Incremental Progress**.
DP asks: *"To reach point $X$, what's the best I could have done?"*
It assumes that the minimum clips to reach point 10 depends on the minimum clips to reach some earlier point $start$.
- If I have a clip `[start, 10]`, then:
  `clips_to_reach_10 = clips_to_reach_start + 1`.
- DP systematically checks *every* possible `start` for *every* possible `end` point. It doesn't "know" which one is best beforehand, so it tries them all and keeps the minimum. It’s like exploring every possible relay hand-off combination to find the fastest one.

---

## Comparison
| Feature | Greedy | Dynamic Programming |
| :--- | :--- | :--- |
| **Intuition** | **Aggressive Efficiency**: Pick the best "giant leap" right now. | **Exhaustive Safety**: Build the best path step-by-step. |
| **Complexity** | $O(N + T)$ | $O(N \cdot T)$ |
| **Analogy** | A scout looking for the longest bridge. | A mason laying bricks one by one. |
