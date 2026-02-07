# LeetCode 350: Intersection of Two Arrays II

This document summarizes the solution for the intersection of two arrays problem and explores efficient Python techniques for dictionary manipulation discussed during the implementation.

## Problem Summary
The goal is to find the intersection of two integer arrays. Each element in the result must appear as many times as it shows in both arrays.

### Solution Approach
The current implementation uses a frequency map (via `defaultdict`) to track occurrences:
1. Count the frequency of each number in `nums1`.
2. Iterate through `nums2`, check if the number exists in the map with a count `> 0`, and if so, add it to the result and decrement the count.

```python
from collections import defaultdict

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = defaultdict(int)
        res = []
        for e in nums1:
            seen[e] += 1
        for e in nums2:
            if e in seen and seen[e] > 0:
                seen[e] -= 1
                res.append(e)
        return res
```

---

## Python Tip: Picking Keys with Specific Values
When you need to filter a dictionary to find keys with a specific value (e.g., `value == 1`), there are several approaches.

### 1. List Comprehension (Recommended)
This is the most "Pythonic" and efficient way.
```python
keys = [k for k, v in my_dict.items() if v == 1]
```

### 2. Dictionary Comprehension (To keep pairs)
```python
filtered_dict = {k: v for k, v in my_dict.items() if v == 1}
```

### 3. Using `filter()`
```python
keys = list(filter(lambda k: my_dict[k] == 1, my_dict))
```

---

## Comparison: `.items()` vs `filter()`

| Feature | `.items()` + Comprehension | `filter()` + `lambda` |
| :--- | :--- | :--- |
| **Speed** | **Faster**: Retrieves key and value in one step. | **Slower**: Performs a hash lookup (`my_dict[k]`) for every key. |
| **Readability** | **High**: Standard syntax, easy to read. | **Lower**: Requires `lambda` and `list()` wrapping. |
| **Overhead** | **Low**: Runs at the C level in Python. | **Higher**: Function call overhead for each element. |

### Conclusion
Always prefer **List/Dictionary Comprehensions** using `.items()` for better performance and cleaner code. Only use `filter()` if you specifically need an iterator and prefer functional programming styles.
