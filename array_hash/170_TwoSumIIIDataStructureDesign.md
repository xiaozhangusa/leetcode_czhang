# TwoSum III - Data Structure Design

## Problem Overview
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

## The Bug
The initial implementation had a critical logical flaw:

```python
    def find(self, value: int) -> bool:
        for i in self.nums:
            if i in self.sum_dict:
                return True
            else:
                self.sum_dict[value - i] = i
        return False
```

### Issues:
1.  **State Persistence**: `self.sum_dict` was an instance variable that persisted across multiple `find()` calls. This meant calculations from a previous search could incorrectly interfere with a new search.
2.  **Missing Imports**: `defaultdict` was used but never imported from `collections`.

## The Solution: Frequency Map
The most efficient and robust way to solve this is using a frequency map (Hash Map).

### Optimized Implementation
By storing the count of each number, we can perform checks in $O(N)$ time (where $N$ is the number of unique elements) and handle duplicates correctly.

```python
from collections import defaultdict

class TwoSum:
    def __init__(self):
        # Use a frequency map to store counts of each number
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        # Increment frequency of the number
        self.count[number] += 1

    def find(self, value: int) -> bool:
        # Iterate through unique numbers in the map
        for num in self.count:
            complement = value - num
            
            # Case 1: Complement is the same as the number (need at least 2 instances)
            if complement == num:
                if self.count[num] > 1:
                    return True
            # Case 2: Complement is different (need at least 1 instance)
            elif complement in self.count:
                return True
                
        return False
```

## Complexity Analysis
- **add(number)**: $O(1)$ time. We just update the hash map.
- **find(value)**: $O(N)$ time, where $N$ is the number of unique integers added.
- **Space Complexity**: $O(N)$ to store the numbers in the hash map.

## Visualization
Imagine adding numbers `[1, 3, 5]`.
- `find(4)`:
    - Look at `1`. Complement is `4 - 1 = 3`. `3` exists. **True**.
- `find(7)`:
    - Look at `1`. Complement is `6`. No.
    - Look at `3`. Complement is `4`. No.
    - Look at `5`. Complement is `2`. No.
    - **False**.
