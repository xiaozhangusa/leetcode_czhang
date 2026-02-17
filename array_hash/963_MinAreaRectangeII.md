# 963. Minimum Area Rectangle II - Comprehensive Guide

## Problem Understanding

Given points in a 2D plane, find the **minimum area** of any rectangle formed by these points. The key difference from the standard rectangle problem is that **sides don't need to be parallel to the X and Y axes** - the rectangle can be rotated at any angle!

## Visual Example

Let's visualize Example 1: `points = [[1,2],[2,1],[1,0],[0,1]]`

```
    Y
    2  •(1,2)
    1  (0,1)•     •(2,1)
    0      •(1,0)
       0   1   2   X
```

These 4 points form a **diamond-shaped rectangle** (rotated 45°) with area = 2.0

## Key Insight: What Makes a Rectangle?

A rectangle has these properties:
1. **4 corners**
2. **Opposite sides are equal and parallel**
3. **All angles are 90°** (perpendicular sides)

### The Diagonal Trick 🎯

The most elegant approach uses **diagonals**:
- A rectangle has **2 diagonals**
- These diagonals **bisect each other** (share the same midpoint)
- The diagonals are **equal in length**

## Approach: Diagonal-Based Solution

### Strategy

1. **Enumerate all possible pairs of points** as potential diagonals
2. **Group diagonal pairs by their midpoint**
3. For diagonals sharing the same midpoint, **check if they form a rectangle**
4. Calculate area and track the minimum

### Why This Works

If two diagonals share the same midpoint, we have 4 points that might form a rectangle. We just need to verify they actually do!

## Step-by-Step Algorithm

### Step 1: Store Diagonals by Midpoint

For every pair of points `(p1, p2)`:
- Calculate **midpoint**: `mid = ((x1+x2)/2, (y1+y2)/2)`
- Calculate **diagonal length squared**: `d² = (x2-x1)² + (y2-y1)²`
- Store as: `midpoint → [(diagonal_vector, length², point_pair)]`

### Step 2: Check Rectangle Conditions

For diagonals sharing the same midpoint:
- They must have **equal length** (rectangle property)
- They must be **perpendicular** (90° angle)

### Step 3: Verify Perpendicularity

Two vectors are perpendicular if their **dot product = 0**:

```
Vector1 = (x1, y1)
Vector2 = (x2, y2)
Dot Product = x1·x2 + y1·y2 = 0  ✓ Perpendicular!
```

### Step 4: Calculate Area

For a rectangle with diagonals `d1` and `d2`:
```
Area = (|d1| × |d2|) / 2
```

Actually, for perpendicular diagonals of equal length in a rectangle:
```
If diagonal length = d
Side lengths can be derived from: a² + b² = d²
Area = a × b
```

But there's an easier formula using the cross product magnitude!

## Detailed Example Walkthrough

### Example: `points = [[1,2],[2,1],[1,0],[0,1]]`

**Step 1: Generate all diagonal pairs**

| Point Pair | Midpoint | Length² | Diagonal Vector |
|------------|----------|---------|-----------------|
| (1,2)-(1,0) | (1, 1) | 4 | (0, 2) |
| (1,2)-(0,1) | (0.5, 1.5) | 2 | (1, 1) |
| (1,2)-(2,1) | (1.5, 1.5) | 2 | (-1, 1) |
| (1,0)-(0,1) | (0.5, 0.5) | 2 | (1, -1) |
| (1,0)-(2,1) | (1.5, 0.5) | 2 | (-1, 1) |
| (0,1)-(2,1) | (1, 1) | 4 | (-2, 0) |

**Step 2: Group by midpoint**

Midpoint `(1, 1)` has:
- Diagonal 1: `(1,2)-(1,0)` with vector `(0, 2)`, length² = 4
- Diagonal 2: `(0,1)-(2,1)` with vector `(-2, 0)`, length² = 4

**Step 3: Check perpendicularity**

```
v1 = (0, 2)
v2 = (-2, 0)
Dot product = 0·(-2) + 2·0 = 0  ✓ Perpendicular!
Length² equal: 4 = 4  ✓ Equal!
```

**Step 4: Calculate area**

```
|v1| = √4 = 2
|v2| = √4 = 2

Area = (|v1| × |v2|) / 2 = (2 × 2) / 2 = 2.0
```

## Implementation Template

```python
from typing import List
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        if n < 4:
            return 0
        
        # Dictionary: midpoint -> list of (diagonal_vector, length², p1, p2)
        diagonals = defaultdict(list)
        
        # Step 1: Generate all possible diagonals
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                
                # Midpoint (use tuple for hashing)
                mid = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
                
                # Diagonal vector
                vec = (p2[0] - p1[0], p2[1] - p1[1])
                
                # Length squared (avoid sqrt for efficiency)
                length_sq = vec[0]**2 + vec[1]**2
                
                diagonals[mid].append((vec, length_sq, p1, p2))
        
        min_area = float('inf')
        
        # Step 2: Check each midpoint with multiple diagonals
        for mid, diag_list in diagonals.items():
            if len(diag_list) < 2:
                continue
            
            # Step 3: Check all pairs of diagonals at this midpoint
            for i in range(len(diag_list)):
                for j in range(i + 1, len(diag_list)):
                    vec1, len1_sq, _, _ = diag_list[i]
                    vec2, len2_sq, _, _ = diag_list[j]
                    
                    # Check if diagonals are equal length
                    if len1_sq != len2_sq:
                        continue
                    
                    # Check if perpendicular (dot product = 0)
                    dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
                    if dot_product != 0:
                        continue
                    
                    # Step 4: Calculate area
                    # For perpendicular diagonals: Area = |d1| × |d2| / 2
                    area = (len1_sq ** 0.5) * (len2_sq ** 0.5) / 2
                    min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0
```

## Why This Approach Works

### Geometric Proof

1. **Diagonals of a rectangle bisect each other** → They share the same midpoint
2. **Diagonals of a rectangle are equal** → `|d1| = |d2|`
3. **For a rectangle (not rhombus), diagonals are perpendicular only if it's a square**

Wait, that's not quite right! Let me clarify:

### Correction: Rectangle vs Rhombus

- **Rectangle**: Diagonals are equal, bisect each other, but NOT necessarily perpendicular
- **Rhombus**: Diagonals are perpendicular, bisect each other, but NOT necessarily equal
- **Square**: Both equal AND perpendicular

So our algorithm actually finds **any quadrilateral** where:
- Diagonals bisect each other (parallelogram)
- Diagonals are equal (rectangle)
- We need to verify it's actually a rectangle!

### Better Approach: Use All 4 Points

Actually, a more robust approach:

1. **Pick any 3 points** as potential corners
2. **Calculate the 4th point** that would complete the rectangle
3. **Check if that 4th point exists** in our set

## Alternative Approach: 3-Point Method

```python
def minAreaFreeRect(self, points: List[List[int]]) -> float:
    point_set = set(map(tuple, points))
    n = len(points)
    min_area = float('inf')
    
    # Try all combinations of 3 points
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[k]
                
                # Try p1 as corner with p2 and p3 as adjacent corners
                # Calculate 4th point: p4 = p2 + p3 - p1
                p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
                
                if p4 not in point_set:
                    continue
                
                # Check if p1-p2 and p1-p3 are perpendicular
                v1 = (p2[0] - p1[0], p2[1] - p1[1])
                v2 = (p3[0] - p1[0], p3[1] - p1[1])
                
                if v1[0] * v2[0] + v1[1] * v2[1] != 0:
                    continue
                
                # Calculate area
                area = (v1[0]**2 + v1[1]**2)**0.5 * (v2[0]**2 + v2[1]**2)**0.5
                min_area = min(min_area, area)
    
    return min_area if min_area != float('inf') else 0
```

## Complexity Analysis

### Diagonal Approach
- **Time**: O(n² × m) where m = max diagonals per midpoint ≈ O(n³) worst case
- **Space**: O(n²) for storing diagonals

### 3-Point Approach
- **Time**: O(n³) for trying all 3-point combinations
- **Space**: O(n) for point set

## Key Takeaways

1. **Rectangles can be rotated** - don't assume axis-aligned!
2. **Use geometric properties**: perpendicularity (dot product = 0)
3. **Diagonal method**: Group by midpoint, check equal length + perpendicular
4. **3-Point method**: Fix 3 corners, calculate 4th, verify perpendicularity
5. **Avoid floating point issues**: Use squared distances when possible

## Common Pitfalls

❌ **Assuming axis-aligned rectangles only**
❌ **Forgetting to check perpendicularity**
❌ **Not handling the case when no rectangle exists**
❌ **Floating point comparison issues** (use epsilon for comparisons)

✅ **Use dot product for perpendicularity**
✅ **Use squared distances to avoid sqrt**
✅ **Return 0 when no rectangle found**
