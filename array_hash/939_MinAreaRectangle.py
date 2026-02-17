# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

# Example 1:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
 

# Constraints:

# 1 <= points.length <= 500
# points[i].length == 2
# 0 <= xi, yi <= 4 * 104
# All the given points are unique.


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0

        # key = len of sides parallel to the x axis
        parallel = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                # parallel check
                if p1[1] - p2[1] == 0:
                    if p1[0] < p2[0]:
                       parallel[abs(p1[0] - p2[0])].append((p1, p2))
                    else:
                        parallel[abs(p1[0] - p2[0])].append((p2, p1))

        res = float(inf)
        for l, pairs in parallel.items():
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    (p1, p2), (p3, p4) = pairs[i], pairs[j]
                    if p1[0] == p3[0] and p2[0] == p4[0]:
                        area = abs(p2[0] - p1[0]) * abs(p3[1] - p1[1])
                        res = min(res, area)
        return res if res < float(inf) else 0