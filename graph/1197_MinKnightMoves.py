# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

# Constraints:

# -300 <= x, y <= 300
# 0 <= |x| + |y| <= 300

from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Use absolute values due to symmetry
        x, y = abs(x), abs(y)
        
        # Directions for a knight move
        dirs = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        step = 0
        
        while q:
            # Level-by-level BFS
            for _ in range(len(q)):
                curr_x, curr_y = q.popleft()
                
                if curr_x == x and curr_y == y:
                    return step
                
                for dx, dy in dirs:
                    nx, ny = curr_x + dx, curr_y + dy
                    
                    # Optimization: Since we target (abs(x), abs(y)), 
                    # we can stay in the positive quadrant mostly.
                    # nx >= -1 and ny >= -1 allows for the knight to move 
                    # slightly negative to reach small positive targets.
                    if (nx, ny) not in visited and nx >= -1 and ny >= -1:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            
            step += 1
        
        return -1 # Should not reach here per constraints
