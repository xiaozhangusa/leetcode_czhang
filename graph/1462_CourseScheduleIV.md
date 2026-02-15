# 1462. Course Schedule IV (Prerequisite Check)

## Problem Context
Unlike the previous Course Schedule problems, this one asks for **transitive** relationships. If `A -> B` and `B -> C`, then `A` is a prerequisite of `C`. 

## The "Amnesia" Bug 🧠
The common pitfall when using Kahn's Algorithm (BFS) for this problem is forgetting to **pass down** inherited prerequisites.

### How the Bug Happens
1. Course **B** enters the queue and learns it needs **A** (`pres[B] = {A}`).
2. Course **B** finishes and unlocks **C**.
3. Course **C** looks at **B** and says, *"Okay, B is my prerequisite."* (`pres[C].add(B)`).
4. **The Failure**: If you don't explicitly tell **C** to look at what **B** already knows, **C** will never learn about **A**. It has "Amnesia" regarding its grandparents.

---

### The Fix: Prerequisite Inheritance
While processing the BFS, when a course `curr` unlocks a child `neighbor`, we must perform a two-step transfer:

```python
# 1. Direct Stamp
ancestors[neighbor].add(curr)

# 2. Transitive Photocopy
ancestors[neighbor].update(ancestors[curr])
```

#### `add()` vs `update()`: The Passport Analogy 🛂
Imagine each course has a **Prerequisite Passport**.

- **`.add(curr)`**: This is like getting a fresh stamp from the current room. 
  - *"I just finished Course A, so Course B gets an 'A' stamp."*
- **`.update(ancestors[curr])`**: This is like **photocopying** every stamp from the previous person's passport into yours.
  - *"If Course A already had stamps for Maths and Physics, Course B now gets those stamps too."*

> [!NOTE]
> **Is anything lost?** No! `.update()` is purely **additive** (a set union). It’s like a **Potluck Dinner**: if you bring a Burger and your friend brings Fries, `.update()` ensures you now have both. The Burger isn't wiped; the plate just gets fuller!

**Without `.update()`**, you only have the most recent stamp. You'd know your teacher, but you'd have no proof that you also finished the teacher's prerequisites!

### ❄️ The "Snowball Effect" (Long Chains)
You asked: *"What about 3, 4, or 5 levels like $A \to B \to C \to D \to E$?"*

Because Kahn's Algorithm (BFS) follows the **Topological Order**, it ensures that a node is only processed **after** all its ancestors are done. This creates a cumulative "Snowball Effect":

1.  **Stage 1 ($A \to B$):** $B$ takes $A$. 
    - `pres[B]` = `{A}`
2.  **Stage 2 ($B \to C$):** $C$ takes $B$ **AND** everything $B$ already has.
    - `pres[C]` = `{B} + {A}` = `{A, B}`
3.  **Stage 3 ($C \to D$):** $D$ takes $C$ **AND** everything $C$ already has.
    - `pres[D]` = `{C} + {A, B}` = `{A, B, C}`
4.  **Stage 4 ($D \to E$):** $E$ takes $D$ **AND** everything $D$ already has.
    - `pres[E]` = `{D} + {A, B, C}` = `{A, B, C, D}`

Essentially, as the BFS "flows" down the chain, the `set` grows larger and larger. By the time you reach the very last course, its `set` contains the **entire history** of the chain above it.

---

### Vivid Analogy: The Family Inheritance 💰
Imagine prerequisites are like **Family Wisdom**:
- **Grandpa A** teaches **Dad B** everything he knows.
- When **Dad B** teaches **Son C**, he must not only teach his own skills but also pass down everything **Grandpa A** taught him. 
- Because **Son C** only starts learning **after** **Dad B** has finished his own education, the wisdom is never lost!

---

## Optimized BFS Implementation

```python
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegrees = [0] * numCourses

        for pre, crs in prerequisites:
            adj[pre].append(crs)
            indegrees[crs] += 1

        # Kahn's Algorithm starting points
        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        
        # Track all ancestors for each node
        ancestors = [set() for _ in range(numCourses)]

        for curr in queue:
            for neighbor in adj[curr]:
                # INHERITANCE STEP:
                ancestors[neighbor].add(curr)
                ancestors[neighbor].update(ancestors[curr])
                
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        # Answer queries in O(1) using the ancestor sets
        return [u in ancestors[v] for u, v in queries]
```

### Performance Note
By using `set.update()`, we ensure that each transitive check in the query phase is $O(1)$. The setup phase remains efficient as each edge and its ancestor set are processed exactly once.
