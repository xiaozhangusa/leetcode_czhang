3.  **Optimal Substructure**: Once I join a fleet, I am trapped by the leader's speed. My original speed no longer affects cars behind me—only the leader's speed does. 

> [!IMPORTANT]
> **The Fleet Speed Rule**: A fleet always moves at the speed of the **slowest car**. If a car taking 1 hour catches a car taking 4 hours, the whole fleet now takes 4 hours. You must track the **maximum** arrival time seen so far to correctly count fleets.

---

## 🧬 The "Rolling Gap" Connection
In the **Interval Mastery Guide**, we discuss the "Rolling Gap" technique. Car Fleet is a "Direct Cousin" of this technique, but with a twist:

- **The Gap**: We aren't looking at the *miles* between cars, but the **Time Gap** in their predicted arrivals at the target.
- **The "Collision"**: If the car behind has a smaller predicted "Time-to-Target", the arrival gap "closes" (becomes zero or negative) before the target.
- **Greedy Maintenance**: Just like **Teemo Attacking (LC 495)** only cares about the *next* attack to see if the timer resets, **Car Fleet** only cares about the **Fleet Leader** directly in front to see if the path is blocked.

---

## 🎯 The Intuition: "The One-Lane Bridge"
Imagine a long, narrow one-lane bridge. Cars are driving toward the end (the `target`).
- A fast car catches up to a slow car.
- The fast car **cannot pass**. It must slow down and follow the leader.
- They now move as a **Fleet** at the speed of the slower car.

### 🧠 The Key Realization
Instead of simulating every second of driving, we focus on **Time to Target**.
- If Car A is ahead of Car B.
- Car A takes $T_A$ hours to finish.
- Car B takes $T_B$ hours to finish.
- If $T_B \leq T_A$, then Car B will eventually "bump" into Car A and join its fleet.
- If $T_B > T_A$, Car B is too slow and will never catch up. It starts its own fleet.

---

## 🛠️ Step-by-Step Strategy

1.  **Sort by Position (Descending)**: We process cars from the one closest to the target to the one furthest away. The car closest to the target is the "Potential Leader" of the first fleet.
2.  **Calculate Time**: for each car, $Time = \frac{Target - Position}{Speed}$.
3.  **Count Fleets**:
    - If a car behind takes **more time** than the current leader, it becomes the **new leader** of a new fleet. 
    - Why? Because it can never catch the car in front, and anyone behind *it* might catch *it*.

### 💡 Developer Tip: The Sentinel Value
In the implementation, we initialize `cur_lead_time = 0`. This is a classic "Sentinel Value" pattern:
- **Automatic First Leader**: Since all arrival times are positive, the first car will always be `> 0`, making it the first fleet leader automatically.
- **Robustness**: It gracefully handles an empty input list without needing an explicit `if not cars` check.
- **Uniform Logic**: Every car (including the first one) is treated with the same `if arrival_time > cur_lead_time` logic.

---

## 📊 Vivid Example

**Input**: `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`

1.  **Sort by Pos Descending**: `(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)`
2.  **Process**:
    - **Car (10, 2)**: Time = $(12-10)/2 = \mathbf{1.0}$. New Fleet! (Count: 1, Lead: 1.0)
    - **Car (8, 4)**: Time = $(12-8)/4 = \mathbf{1.0}$. $1.0 \leq 1.0$, joins Fleet 1.
    - **Car (5, 1)**: Time = $(12-5)/1 = \mathbf{7.0}$. $7.0 > 1.0$, **New Fleet!** (Count: 2, Lead: 7.0)
    - **Car (3, 3)**: Time = $(12-3)/3 = \mathbf{3.0}$. $3.0 \leq 7.0$, joins Fleet 2.
    - **Car (0, 1)**: Time = $(12-0)/1 = \mathbf{12.0}$. $12.0 > 7.0$, **New Fleet!** (Count: 3, Lead: 12.0)

**Result**: 3 Fleets.

---

## 🚀 Complexity
- **Time**: $O(N \log N)$ due to sorting the positions.
- **Space**: $O(N)$ for the sorted list of pairs (or $O(1)$ if we only count the stack-like tracking).
