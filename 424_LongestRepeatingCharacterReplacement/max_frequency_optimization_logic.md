# Max Frequency Optimization in Sliding Window

In the [Solution.canReplace](file:///Users/chi/projects/practice/leetcode_czhang/424_LongestRepeatingCharacterReplacement/424_LongestRepeatingCharacterReplacement.py#L42) function, you might wonder why updating `maxFreq` with `max(maxFreq, freq[s[end]])` works, even though we never decrement it when shrinking the window.

## The Logic: "Only Care About Improvement"

The goal of the `canReplace` function is to find if **any** window of size `sublen` is valid. A window is valid if:
`sublen - (count of the most frequent character) <= k`

### 1. Why a "Leaky" `maxFreq` Works
If we use a `maxFreq` that only increases, it represents the **maximum frequency of any character seen in any window of the current `sublen` handled so far.**

*   **If the real max frequency drops:** Suppose 'A' was the most frequent character (freq 5), but it just left the window, and now the most frequent character has freq 3.
*   The current window is **worse** than the previous one.
*   Since the previous window (with freq 5) didn't satisfy the `sublen - maxFreq <= k` condition (otherwise we would have already returned `True`), the current window (with freq 3) definitely won't either.
*   We only need `maxFreq` to be accurate when it's high enough to make the window "good."

### 2. Correctness for Binary Search
Because we are searching for a **fixed** `sublen`, if *any* window of that size in the string is valid, then at some point during the loop, `freq[s[end]]` will reach its peak value for that window, making the condition `sublen - maxFreq <= k` true.

Even if `maxFreq` becomes "stale" (referring to a character that left the window), it doesn't cause false positives. If `maxFreq` is 10, it means some character *did* appear 10 times in a window of size `sublen`. If that was enough to satisfy the condition, the function would have returned `True` already.

## 3. Efficiency

| Method | Complexity | Reason |
| :--- | :--- | :--- |
| `max(freq.values())` | $O(26)$ | Must scan the entire dictionary/frequency array every slide. |
| `max(maxFreq, freq[s[end]])` | $O(1)$ | Only compares two integers. |

## 4. Implementation Tip

To ensure `maxFreq` is as accurate as possible for the current window, it's best to update it **after** shifting the start pointer:

```python
if end + 1 - start > sublen:
    freq[s[start]] -= 1
    start += 1
# Update after sliding to reflect the new window content
maxFreq = max(maxFreq, freq[s[end]])
```
