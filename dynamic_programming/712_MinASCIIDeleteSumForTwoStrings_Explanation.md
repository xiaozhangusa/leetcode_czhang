# Minimum ASCII Delete Sum for Two Strings - Bug Analysis

The original implementation of the `minimumDeleteSum` function contained several fundamental logic errors. This document outlines why the code was buggy and provides the correct approach.

## 1. Metric Mismatch (ASCII Sum vs. Count)

**The Bug:**
The code attempted to use a standard Longest Common Subsequence (LCS) or Edit Distance style transition:
```python
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
```
It added `+ 1` for each deletion.

**The Fix:**
The problem asks for the **minimum ASCII sum** of deleted characters. We must add the ASCII value of the character being deleted:
```python
dp[i][j] = min(dp[i - 1][j] + ord(s1[i-1]), dp[i][j - 1] + ord(s2[j-1]))
```

## 2. Missing Base Case Initialization

**The Bug:**
The DP table was initialized with all zeros:
```python
dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
```
While this works for problems like LCS, it fails here because deleting characters to match an empty string has a non-zero cost (the ASCII sum of the deleted characters).

**The Fix:**
The first row and column must be initialized with the prefix sums of the ASCII values of the respective strings:
- `dp[i][0]` is the sum of characters in `s1[0:i]`.
- `dp[0][j]` is the sum of characters in `s2[0:j]`.

## 3. Broken Backtracking Logic

**The Bug:**
The code tried to solve the problem by counting deletions and then backtracking to find the ASCII sum:
```python
elif dp[i][j] == dp[i - 1][j]:
    res += int(s1[i])  # Error 1: s1[i] is a char, int() fails. Should be ord().
    i -= 1             # Error 2: Off-by-one index (s1[i] vs s1[i-1]).
```
This backtracking was inherently flawed because the `dp` table itself was built using counts, not sums, so it wouldn't necessarily find the path that minimizes the ASCII sum.

## 4. Correct DP Strategy

By building the `dp` table where `dp[i][j]` directly represents the minimum ASCII sum to make `s1[:i]` and `s2[:j]` equal, the final answer is simply `dp[l1][l2]`. No backtracking is needed.

### Optimal Substructure
- If `s1[i-1] == s2[j-1]`, no deletion is needed for these characters: `dp[i][j] = dp[i-1][j-1]`.
- If they differ, we take the minimum of:
    1. Deleting `s1[i-1]`: `dp[i-1][j] + ord(s1[i-1])`
    2. Deleting `s2[j-1]`: `dp[i][j-1] + ord(s2[j-1])`

## 5. DP Table Visualization (Example: "sea" vs "eat")

Here is how the table is populated step-by-step.

**ASCII Values:**
- `s`: 115, `e`: 101, `a`: 97
- `e`: 101, `a`: 97, `t`: 116

| | "" | **e** (101) | **a** (97) | **t** (116) |
| :--- | :---: | :---: | :---: | :---: |
| "" | 0 | 101 | 198 | 314 |
| **s** (115) | 115 | 216 | 313 | 429 |
| **e** (101) | 216 | 115 | 212 | 328 |
| **a** (97) | 313 | 212 | 115 | **231** |

**How to read the table:**
1.  **Row 0 & Col 0**: Cumulative sum of deleting characters to reach an empty string.
2.  **dp[2][1] (e vs e)**: Since characters match, we take diagonally: `dp[1][0] = 115`.
3.  **dp[3][3] (a vs t)**: Since characters differ, we take `min(dp[2][3] + 97, dp[3][2] + 116) = min(328 + 97, 115 + 116) = 231`.
