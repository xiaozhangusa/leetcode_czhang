# Design Compressed String Iterator Clarification

The problem asks us to design an iterator that "uncompresses" a string on-the-fly.

A compressed string looks like: `L1e2t1C1o1d1e1`
- `L1` means 'L' appears 1 time.
- `e2` means 'e' appears 2 times.
- `t1` means 't' appears 1 time.
- The uncompressed version is: `LeetCode`

---

## 🍬 The Candy Dispenser Analogy

Imagine a physical candy dispenser (like a PEZ dispenser) loaded with different flavors of candy.

### `next()`: Dispensing one candy at a time
Every time you call `next()`, you are pushing the button once.
- **Example**: If you have `e2`, the first `next()` gives you one 'e'. The second `next()` gives you the last 'e'.
- **Running out**: If the dispenser is empty and you keep pushing the button, you get a "blank" (a white space `' '`).

### `hasNext()`: Checking if the dispenser is empty
This is like looking through the clear plastic window of the dispenser.
- **Example**: If there is even **one** candy left inside, `hasNext()` is `True`.
- **Empty**: Only when every single character from every group (like `L1`, `e2`) has been dispensed does `hasNext()` become `False`.

---

## 🚀 Vivid Step-by-Step Example

Let's use `a2b1`:

| Step | Action | Result | Remaining (Internal State) |
| :--- | :--- | :--- | :--- |
| 1 | `hasNext()` | `True` | There are two 'a's and one 'b' left. |
| 2 | `next()` | `'a'` | One 'a' and one 'b' left. |
| 3 | `next()` | `'a'` | Only one 'b' left. |
| 4 | `hasNext()` | `True` | Still have that 'b'! |
| 5 | `next()` | `'b'` | **Empty!** |
| 6 | `hasNext()` | `False` | Nothing left. |
| 7 | `next()` | `' '` | Dispensing a blank. |

---

## 💡 Key Insight
The iterator doesn't uncompress the whole string at once (which could be huge, like `a1000000000`). It just keeps track of:
1. Which character it's currently on.
2. How many of *that* character are left before moving to the next group.

---

## 🔍 Unfolding the Regex: `re.findall(r'([a-zA-Z])(\d+)', ...)`

The parsing logic uses a powerful regular expression to "sweep" the string and extract pairs:

1.  **`([a-zA-Z])`**: Catches exactly **one** letter (the "flavor").
2.  **`(\d+)`**: Catches **one or more** digits (the "quantity"). This allows it to handle `A10` just as easily as `A1`.
3.  **`re.findall`**: Automatically groups these into a list of tuples like `[('L', '1'), ('e', '2'), ...]`.

This avoids a messy manual loop to check `isdigit()` and reconstruct numbers!

### 🧩 Why the Tuples? (Python's `re.findall` Rules)

These "rules" are the standard behavior built into Python's `re` module. When you use `re.findall(pattern, string)`, Python decides what to return based on the number of **capturing groups** (parentheses) in your pattern:

*   **No parentheses**: Returns the full matching string.
    *   `re.findall(r'[a-zA-Z]\d+', 'L10')` -> `['L10']`
*   **1 group `(...)`**: Returns only the text caught in that group.
    *   `re.findall(r'([a-zA-Z])\d+', 'L10')` -> `['L']`
*   **2 or more groups**: Returns a **tuple** for each match, containing every group's snapshot.
    *   `re.findall(r'([a-zA-Z])(\d+)', 'L10')` -> `[('L', '10')]`

In our `StringIterator`, we have exactly **two** groups (one for the letter, one for the count), so we get a list of tuples with two items each. This is why we can pull them out so easily in our code!

---

## 🛠️ Implementation Summary

We use a regular expression `([a-zA-Z])(\d+)` to split the compressed string into "flavor groups" (e.g., `'a'` and `2`). We then:
- Use a **cursor** to track which group we are currently dispensing.
- Maintain a **remaining_count** for the current group.
- Return `' '` if we try to dispense when no characters are left.

### Final Python Solution
```python
import re

class StringIterator:
    def __init__(self, compressedString: str):
        self.tokens = re.findall(r'([a-zA-Z])(\d+)', compressedString)
        self.cursor = 0
        self.current_char = self.tokens[0][0] if self.tokens else ''
        self.remaining_count = int(self.tokens[0][1]) if self.tokens else 0

    def next(self) -> str:
        if not self.hasNext(): return ' '
        res = self.current_char
        self.remaining_count -= 1
        if self.remaining_count == 0:
            self.cursor += 1
            if self.cursor < len(self.tokens):
                self.current_char = self.tokens[self.cursor][0]
                self.remaining_count = int(self.tokens[self.cursor][1])
        return res

    def hasNext(self) -> bool:
        return self.remaining_count > 0 or self.cursor < len(self.tokens) - 1
```
