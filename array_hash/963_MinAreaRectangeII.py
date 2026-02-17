# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

# Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:


# Input: points = [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
# Example 2:


# Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
# Example 3:


# Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
 

# Constraints:

# 1 <= points.length <= 50
# points[i].length == 2
# 0 <= xi, yi <= 4 * 104
# All the given points are unique.

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        if n < 4:
            return 0

        diagonals = defaultdict(list)

        # build diagnoals(mid, l) 
        for i in range(len(points)):
            for j in range(i, len(points)):
                p1, p2 = points[i], points[j]
                mid = ((p1[0] + p2[0] / 2), (p1[1] + p2[1] / 2))
                d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                diagonals[(mid, d)].append((p1, p2))

        ans = float(inf)

        for k, pairs in diagonals.items():
            if len(pairs) < 2:
                continue
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    p1, p2 = pairs[i], pairs[j]
                    area = sqrt((p1[0] - p2[0]) * (p1[1] - p2[1]))
                    ans = min(ans, area)

        return ans if ans < float(inf) else 0 