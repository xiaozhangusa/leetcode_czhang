# String Compression (LeetCode 443)

## Problem Description

Given an array of characters `chars`, compress it using the following algorithm:

1. Begin with an empty string `s`.
2. For each group of consecutive repeating characters in `chars`:
    - If the group's length is 1, append the character to `s`.
    - Otherwise, append the character followed by the group's length.
3. The compressed string `s` should not be returned separately, but instead, be stored in the input character array `chars`.
4. Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.
5. Return the new length of the array.

**Constraints:**
- Use only **constant extra space**.
- Modify the input array **in-place**.

## Two-Pointer Strategy

To achieve $O(1)$ extra space, we use two pointers: `read` and `write`.

1. **`read` pointer**: Iterates through the original array to identify groups of identical characters.
2. **`write` pointer**: Keeps track of where to write the compressed character and its count back into the `chars` array.

### Step-by-Step Logic
- We start both `read` and `write` at index 0.
- While `read` is within the bounds of the array:
    - Identify the current character and count how many times it repeats consecutively.
    - Write the character at the `write` position and increment `write`.
    - If the count is greater than 1:
        - Convert the count to a string (e.g., `12` becomes `"1"`, `"2"`).
        - Write each digit of that string into the `chars` array at the `write` position, incrementing `write` each time.
- Finally, return `write`, which represents the new length of the compressed array.

## Time and Space Complexity

- **Time Complexity**: $O(n)$, where $n$ is the length of the input array. We traverse the array once with the `read` pointer.
- **Space Complexity**: $O(1)$ extra space (excluding the space used for the string representation of counts, which is logarithmic with respect to the count and thus very small/constant for practical purposes).

## Vivid Example Walkthrough

### Input: `chars = ["a","a","b","b","c","c","c"]`

| Step | `read` index | `char` | `count` | Action | `chars` State | `write` index |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | 0 | - | - | Initial state | `["a","a","b","b","c","c","c"]` | 0 |
| **1** | 0 -> 2 | 'a' | 2 | Write 'a', then '2' | `["a","2","b","b","c","c","c"]` | 2 |
| **2** | 2 -> 4 | 'b' | 2 | Write 'b', then '2' | `["a","2","b","2","c","c","c"]` | 4 |
| **3** | 4 -> 7 | 'c' | 3 | Write 'c', then '3' | `["a","2","b","2","c","3","c"]` | 6 |
| **End** | 7 | - | - | Return `write` (6) | `["a","2","b","2","c","3",...]` | 6 |

**Output: 6**

## Common Pitfalls to Avoid

When implementing this using two pointers, avoid these logical traps:

### 1. Overwriting your own data
Start writing digits *after* the character. If you use a slice like `chars[j : j + len(str_group_len)] = str_group_len` where `j` is the start index, you will overwrite the character you just wrote.
- **Wrong**: `j` points to the char, then digits overwrite `j`.
- **Right**: Write char at `write`, increment `write`, then write digits at `write`.

### 2. Incorrect Pointer Advancement
The `write` pointer should only advance by the number of characters you actually put in the array (**1** for the char + **len(count_str)**).
- **Wrong**: `j += group_len` skips over the "empty" space you just created by compressing. This results in the original length being returned instead of the compressed one.

### 3. Read/Write Pointer Confusion
Never increment your **read** pointer using the **write** pointer's value (e.g., `i += j + group_len`). This causes the scanning logic to jump ahead or out of bounds because `j` is an index in the modified array, while `i` is an index in the original data.

