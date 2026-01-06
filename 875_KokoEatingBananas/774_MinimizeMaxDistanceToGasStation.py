# You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

# You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

# Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

# Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

 

# Example 1:

# Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
# Output: 0.50000
# Example 2:

# Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
# Output: 14.00000
 

# Constraints:

# 10 <= stations.length <= 2000
# 0 <= stations[i] <= 108
# stations is sorted in a strictly increasing order.
# 1 <= k <= 106

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        l = max(stations) / (len(stations) + k)
        r = max(stations)
        while l < r:
            m = (l + r) / 2
            if self.canAdd(stations, k, m):
                # can add, want to try smaller penalty, inclusively
                r = m
            else:
                # can't add, want to try larger penalty, exclusively
                l = m+1
        return l    
    
    def canAdd(self, stations: List[int], k: int, penalty: float) -> bool:
        for i in range(1, len(stations)):
            if stations[i] - stations[i-1] <= penalty:
                # skip
                continue
            else:
                # need to place a gas station in between stations[i-1] and stations[i]
                k -= math.floor((stations[i] - stations[i-1]) / penalty)
                if k < 0:
                    return False
        return True