# 2085. Count Common Words With One Occurrence

## Problem Description

Given two string arrays `words1` and `words2`, return the number of strings that appear **exactly once** in each of the two arrays.

### Example 1:
- **Input**: `words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]`
- **Output**: `2`
- **Explanation**: 
    - "leetcode" appears once in `words1` and once in `words2`. (Count +1)
    - "amazing" appears once in `words1` and once in `words2`. (Count +1)
    - "is" appears twice in `words1`, so it's disqualified even though it's in `words2`.
    - "as" appears once in `words1` but not in `words2`.
    - Total = 2.

## Buggy Implementation Analysis

The following code snippet was identified as buggy:

```python
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        seen = {}
        for w in words1:
            if w not in seen:
                seen[w] = 1
        for w in words2:
            if w in seen:
                seen[w] -= 1
        res = [k for k, v in seen.items() if v == 0]
        return len(res)
```

### Why it fails:

1.  **Duplicate handling in `words1`**: The logic `if w not in seen: seen[w] = 1` only tracks if a word has been seen *at all*. If a word appears multiple times in `words1`, it is still stored as `1`. The problem requires it to appear **exactly once**.
2.  **Insufficient check for `words2`**: The logic `seen[w] -= 1` for `words2` doesn't verify that the word appears exactly once in `words2`. If a word appears once in `words1` (marked as 1) and twice in `words2`, the counter becomes `-1`, which is not `0`, so it correctly fails that case. However, combined with the first bug, it leads to incorrect results.
    - For example: if `words1 = ["a", "a"]` and `words2 = ["a"]`. 
        - `words1` loop: `seen["a"] = 1`.
        - `words2` loop: `seen["a"]` becomes `0`.
        - Result is `1`, but it should be `0`.

## Correct Solution

The most robust and readable way to solve this is using two frequency maps (or `collections.Counter` in Python) to track the exact count of each word in both arrays.

```python
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Count frequencies in both arrays
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # A word is counted if its frequency is exactly 1 in both maps
        ans = 0
        for w in count1:
            if count1[w] == 1 and count2[w] == 1:
                ans += 1
        return ans
```

### Complexity Analysis
- **Time Complexity**: $O(N + M)$, where $N$ and $M$ are the lengths of `words1` and `words2` respectively. We iterate through each array once to build the counters.
- **Space Complexity**: $O(N + M)$ to store the frequencies in the dictionaries.
