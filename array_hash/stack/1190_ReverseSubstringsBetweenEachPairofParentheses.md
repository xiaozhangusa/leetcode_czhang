# 1190. Reverse Substrings Between Each Pair of Parentheses

## Problem Description
You are given a string `s` that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
The result should not contain any brackets.

**Example:**
Input: `s = "(u(love)i)"`
Output: `"iloveu"`
Explanation:
1. Reverse "love" -> "evol"
2. String becomes "(u(evol)i)"
3. After removing inner brackets: "(uevoli)"
4. Reverse "uevoli" -> "iloveu"

---

## 💡 The "Stack of Strings" Strategy
The most intuitive way to handle nested reversals is to treat each level of parentheses as a separate "drawing board".

1.  **Start a new level** whenever you see an opening parenthesis `(`.
2.  **Write characters** on the current level's board.
3.  **Finish a level** when you see a closing parenthesis `)`. Reverse the current board's content and **hand it back** to the board one level up.

### 🎬 Vivid Step-by-Step: `(u(love)i)`

Imagine we have a stack of boards. We start with Board 0.

| Step | Char | Action | Boards Stack | Current Board Content |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `(` | **Push** new Board | `["", ""]` | `""` (Board 1) |
| 2 | `u` | **Write** to Board 1 | `["", "u"]` | `"u"` |
| 3 | `(` | **Push** new Board | `["", "u", ""]` | `""` (Board 2) |
| 4 | `love`| **Write** to Board 2 | `["", "u", "love"]` | `"love"` |
| 5 | `)` | **Pop**, Reverse, & Merge | `["", "uevol"]` | `"uevol"` |
| 6 | `i` | **Write** to Board 1 | `["", "uevoli"]` | `"uevoli"` |
| 7 | `)` | **Pop**, Reverse, & Merge | `["iloveu"]` | `"iloveu"` |

**Final Result**: `iloveu`

---

## 🛠️ Implementation

```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Each level of parentheses gets its own empty string in the stack
        stack = ['']
        for char in s:
            if char == '(':
                # New level: start a fresh empty string
                stack.append('')
            elif char == ')':
                # Level end: pop the current string, reverse it, 
                # and append to the predecessor level
                reversed_segment = stack.pop()[::-1]
                stack[-1] += reversed_segment
            else:
                # Normal character: just append to the current level
                stack[-1] += char
        
        # The base level contains our final answer
        return stack[0]
```

## 📊 Complexity Analysis

### Time Complexity: $O(N^2)$
In the worst case (e.g., nested parentheses like `(((...)))`), a character can be reversed and concatenated multiple times.
- We iterate through the string of length $N$ once: $O(N)$.
- Inside the loop, string slicing `[::-1]` and concatenation can take up to $O(N)$.
- Total: $O(N \times N) = O(N^2)$.
- *Note*: Given the constraint $N \le 2000$, $O(N^2)$ is well within the time limit.

### Space Complexity: $O(N)$
- The stack stores characters from the input string.
- In the worst case, the stack strings combined will have $N$ characters.
- Thus, the space used is proportional to the input size: $O(N)$.

---

## 🚀 Why this is better than the original attempt
The original code tried to use a flat character stack and a separate `res` array, which made tracking *which* level was being reversed extremely difficult. By using a **stack of strings**, we naturally mirror the nested structure of the parentheses.
