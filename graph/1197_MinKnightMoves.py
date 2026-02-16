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

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2,-1)]
        q = deque([(0, 0)])
        print("q: ", q)
        step = 0
        visited = set()
        while q:
            cur = q.popleft()
            print("cur: ", cur)
            visited.add(cur)
            if cur[0] == x and cur[1] == y:
                return step
            step += 1
            for dx, dy in dirs:
                nx = (cur[0] + dx, cur[1] + dy)
                if nx not in visited:
                    q.append(nx)
