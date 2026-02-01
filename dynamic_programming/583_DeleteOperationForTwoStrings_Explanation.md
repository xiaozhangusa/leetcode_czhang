# 583. Delete Operation for Two Strings - Explanation

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of steps required to make `word1` and `word2` the same. In one step, you can delete exactly one character in either string.

### Example
- **Input:** `word1 = "sea"`, `word2 = "eat"`
- **Output:** `2`
- **Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

---

## The Issues

### 1. IndexError
The original code encountered an `IndexError`:
```python
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        print("word1[i]: ", i, word1[i]) # IndexError here
```
**Why?**
The loops iterate from `1` to `l1` (inclusive). While `dp[i]` is valid because it has size `l1 + 1`, `word1[i]` is out of range because Python strings are 0-indexed. The maximum index for `word1` is `l1 - 1`.

**Fix:**
Access the strings using `i - 1` and `j - 1`:
```python
if word1[i - 1] == word2[j - 1]:
```

### 2. Incomplete DP Logic
The original transition only considered deleting from `word1`:
```python
else:
    # try delete last char from word1
    dp[i][j] = dp[i - 1][j] + 1
```
**Why?**
To find the *minimum* distance, we must consider all possible deletions:
1. Delete from `word1` (moving from `dp[i-1][j]`)
2. Delete from `word2` (moving from `dp[i][j-1]`)

**Fix:**
```python
else:
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
```

---

## Dynamic Programming Approach

### DP Table Definition
`dp[i][j]` represents the minimum number of deletions needed to make `word1[0...i-1]` and `word2[0...j-1]` identical.

### Base Cases
- `dp[i][0] = i`: To make a string of length `i` match an empty string, we must perform `i` deletions.
- `dp[0][j] = j`: Similar logic for an empty `word1`.

### Transitions
- **If `word1[i-1] == word2[j-1]`**: The characters match, so no new deletion is needed.
  `dp[i][j] = dp[i-1][j-1]`
- **If `word1[i-1] != word2[j-1]`**: We must delete one character from either `word1` or `word2`.
  `dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1`

---

## Step-by-Step DP Table (sea vs eat)

Let's trace how the table is populated for `word1 = "sea"` and `word2 = "eat"`.

### 1. Visualization of Indexing Fix
The DP table has dimensions `(len(word1)+1) x (len(word2)+1)`. The row index `i` corresponds to the first `i` characters of `word1`.

| Row index `i` | String prefix | Character matched | Row in Original Code (`word1[i]`) | Row in Correct Code (`word1[i-1]`) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | "s" | 's' | 'e' (word1[1]) ❌ | 's' (word1[0]) ✅ |
| 2 | "se" | 'e' | 'a' (word1[2]) ❌ | 'e' (word1[1]) ✅ |
| 3 | "sea" | 'a' | IndexError ❌ | 'a' (word1[2]) ✅ |

### 2. Table Population (Correct Logic)
**Target:** `word1 = "sea"`, `word2 = "eat"`

#### Base Case (Initialization)
We fill the first row and first column with the number of deletions needed to match an empty string.

| | "" | e | a | t |
| :--- | :--- | :--- | :--- | :--- |
| **""** | **0** | 1 | 2 | 3 |
| **s** | 1 | | | |
| **e** | 2 | | | |
| **a** | 3 | | | |

#### Filling the Table (Step-by-Step)

| Step | i, j | Characters | Match? | Calculation | Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | (1,1) | 's' vs 'e' | No | `min(dp[0][1], dp[1][0]) + 1` = `min(1, 1) + 1` | 2 |
| 2 | (1,2) | 's' vs 'a' | No | `min(dp[0][2], dp[1][1]) + 1` = `min(2, 2) + 1` | 3 |
| 3 | (1,3) | 's' vs 't' | No | `min(dp[0][3], dp[1][2]) + 1` = `min(3, 3) + 1` | **4** |
| 4 | (2,1) | 'e' vs 'e' | **Yes** | `dp[1][0]` | **1** |
| 5 | (2,2) | 'e' vs 'a' | No | `min(dp[1][2], dp[2][1]) + 1` = `min(3, 1) + 1` | 2 |
| 6 | (2,3) | 'e' vs 't' | No | `min(dp[1][3], dp[2][2]) + 1` = `min(4, 2) + 1` | 3 |
| 7 | (3,1) | 'a' vs 'e' | No | `min(dp[2][1], dp[3][0]) + 1` = `min(1, 3) + 1` | 2 |
| 8 | (3,2) | 'a' vs 'a' | **Yes** | `dp[2][1]` | **1** |
| 9 | (3,3) | 'a' vs 't' | No | `min(dp[2][3], dp[3][2]) + 1` = `min(3, 1) + 1` | **2** |

#### Population Sequence

The nested loops in the code ensure we fill the table **row-by-row**, starting from the top-left (1,1) and ending at the bottom-right (3,3).

```python
for i in range(1, l1 + 1):    # Rows (word1)
    for j in range(1, l2 + 1):  # Columns (word2)
```

**Order of operations:**
1.  **Row 1**: (1,1) → (1,2) → (1,3)
2.  **Row 2**: (2,1) → (2,2) → (2,3)
3.  **Row 3**: (3,1) → (3,2) → (3,3)

This sequence satisfies all dependencies. To calculate `dp[i][j]`, we need the values from **above**, **left**, and **diagonal upper-left**, all of which are already computed:

```text
(i-1, j-1)  (i-1, j)
    ↘          ↓
(i, j-1)  → (i, j)
```

---

### 3. Comparison of Logic: Why the original was wrong

The original code (ignoring the `IndexError`) used: `dp[i][j] = dp[i-1][j] + 1` for ALL mismatches.

#### **Original Logic (Incorrect Trace)**
| | "" | e | a | t |
| :--- | :--- | :--- | :--- | :--- |
| **""** | 0 | 1 | 2 | 3 |
| **s** | 1 | 2 (1+1) | 3 (2+1) | 4 (3+1) |
| **e** | 2 | **1** (match) | 4 (3+1) | 5 (4+1) |
| **a** | 3 | 2 (1+1) | **1** (match) | **6** (5+1) ❌ |

**Why it's wrong:**
The original logic was **blind to deletions from `word2`**. It only knew how to delete from `word1`.
- For `dp[2][2]` (se vs ea), it only tried `dp[1][2] + 1 = 4`, refusing to see that `dp[2][1] + 1 = 2` (deleting 'a' from word2) was better.
- Ultimately, it would conclude you need **6** steps to make "sea" and "eat" same (by deleting everything), because it misses the "ea" commonality.

#### **Correct Logic (Current Fix)**
| | "" | e | a | t |
| :--- | :--- | :--- | :--- | :--- |
| **""** | 0 | 1 | 2 | 3 |
| **s** | 1 | 2 | 3 | 4 |
| **e** | 2 | **1** | 2 | 3 |
| **a** | 3 | 2 | **1** | **2** ✅ |

---

## Deletions vs. Standard Edit Distance

In the **Standard Edit Distance** (Levenshtein Distance), we have three operations: Insert, Delete, and Replace. In this problem, we **only** have Deletion.

### 1. The Perspective Shift
In standard Edit Distance, we usually ask: *"How many operations to transform `word1` into `word2`?"* This means:
- **Delete**: Remove a character from `word1`.
- **Insert**: Add a character to `word1`.
- **Replace**: Change a character in `word1`.

In **this problem**, the question is: *"How many deletions to make both strings the same?"* 
Because you can delete from **either** string, the operations become symmetric.

### 2. The Mathematical Symmetry
**An "Insert" into `word1` is mathematically equivalent to a "Delete" from `word2`.**

Let's look at the DP transition's "No Match" cases:

| Logic in DP | Action in this problem | Standard Edit Distance View |
| :--- | :--- | :--- |
| `dp[i-1][j] + 1` | Delete `word1[i-1]` | **Delete** (remove from source) |
| `dp[i][j-1] + 1` | Delete `word2[j-1]` | **Insert** (add to source to match target) |

#### Example: `word1 = "ab"`, `word2 = "abc"`
- **To make them same by deleting**: You delete 'c' from `word2`. (1 step)
- **To transform `ab` → `abc`**: You insert 'c' into `word1`. (1 step)

### 3. Vivid Examples: Why Insert == Delete

Imagine you have two strings, and you are trying to align them by placing characters into "slots". When characters don't match, you must create a **Gap** (`-`).

#### Example: Aligning "ab" and "abc"

Imagine a "Cursor" pointing at the current characters we are trying to match.

**Scenario A: "I'm word1, I will INSERT 'c'"**
```text
word1:  a  b [c]  <-- You added a new character 'c'
word2:  a  b  c   <-- This character now matches word2
```
- In the DP table, this means you satisfied `word2`'s 'c' but didn't "use up" any character from your original `word1`. 
- **State move**: `dp[i][j]` depends on `dp[i][j-1]` (same row, previous column).

**Scenario B: "I'm word2, I will DELETE 'c'"**
```text
word1:  a  b      <-- You stay the same
word2:  a  b (c)  <-- You throw 'c' in the trash
```
- In the DP table, this also means you are looking at the same prefix of `word1` but you've moved past 'c' in `word2`.
- **State move**: `dp[i][j]` depends on `dp[i][j-1]`.

#### The "Mirror" Effect
Whether you call it an **Insertion** in `word1` or a **Deletion** from `word2`, the physical alignment looks exactly the same:

| String | Slot 1 | Slot 2 | Slot 3 |
| :--- | :--- | :--- | :--- |
| **word1** | a | b | **- (GAP)** |
| **word2** | a | b | **c** |

- **Looking from top to bottom**: "There is a gap in `word1`, I need to **Insert** 'c'."
- **Looking from bottom to top**: "There is an extra 'c' in `word2` compared to `word1`, I need to **Delete** 'c'."

### 4. Deep Dive: What does `dp[i][j-1]` really mean?

Let's simplify. Forget "Gaps" and think about **Two Pointers** moving along the strings.

#### The State Definition
- `i`: Pointer to the end of the part of `word1` we are currently looking at.
- `j`: Pointer to the end of the part of `word2` we are currently looking at.

#### The "Pointer Race" Visualization
Imagine you are trying to reach the destination `dp[i][j]`. To get there, you must have successfully **processed** (or "accounted for") everything up to index `i` in `word1` and `j` in `word2`.

When you move from `dp[i][j-1]` to `dp[i][j]`:

| Pointer | Previous State `dp[i][j-1]` | Current State `dp[i][j]` | Result |
| :--- | :--- | :--- | :--- |
| **`word1` Pointer** | At index `i` | At index `i` | **Stayed still** (No new char) |
| **`word2` Pointer** | At index `j-1` | At index `j` | **Advanced** (New char `word2[j-1]`) |

#### "Satisfied word2" vs "Didn't use up word1"
1.  **"Satisfied `word2`"**: This means the `word2` pointer successfully moved forward. You have now **finished dealing with** its new character `word2[j-1]`.
2.  **"Didn't use up `word1`"**: This means the `word1` pointer didn't move. You are using the **exact same prefix** of `word1` that you had in the previous step.

#### The "Vivid" Reasoning
If `word2` moved forward but `word1` didn't, how did you "deal with" that new character in `word2`?
- **Since you didn't move the `word1` pointer to find a match, the only way to "account for" that new character is to DELETE it.**

#### Example: `word1 = "A"`, `word2 = "AB"`
- `dp[1][1]` (A vs A): Cost = 0.
- Now look at `dp[1][2]` (A vs AB):
    - You want to finish `word2` (move pointer from 'A' to 'B').
    - You decide **not** to move the pointer in `word1` (it stays at 'A').
    - To move past the 'B' in `word2` without a matching character in `word1`, you pay **+1 deletion** from `word2`.
    - `dp[1][2] = dp[1][1] + 1 = 1`.

### 5. Quick Summary: The Deletion Mapping

Yes, your interpretation is exactly correct! Here is the definitive map:

| DP Move | Action | Meaning |
| :--- | :--- | :--- |
| **`dp[i-1][j] + 1`** | **Delete from `word1`** | `word1` pointer moved forward, but `word2` pointer stayed still. The extra character in `word1` was thrown away. |
| **`dp[i][j-1] + 1`** | **Delete from `word2`** | `word2` pointer moved forward, but `word1` pointer stayed still. The extra character in `word2` was thrown away. |
| **`dp[i-1][j-1]`** | **Keep Both** | (Only if characters match) Both pointers moved forward together because they "found" each other. Cost is 0. |

---
