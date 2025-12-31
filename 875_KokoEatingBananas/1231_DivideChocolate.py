# You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

# You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

# Example 1:

# Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
# Output: 6
# Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
# Example 2:

# Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
# Output: 1
# Explanation: There is only one way to cut the bar into 9 pieces.
# Example 3:

# Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
# Output: 5
# Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

# Constraints:

# 0 <= k < sweetness.length <= 104
# 1 <= sweetness[i] <= 105

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l, r = min(sweetness), sum(sweetness)
        while l < r:
            mid = (l + r) // 2
            # inclusively
            if self.canCut(sweetness, mid, k):
                r = mid
            # exclusively
            else:
                l = mid + 1
        return l
    
    def canCut(self, sweetness: List[int], minSweet: int, k: int) -> bool:
        print("new round")
        s, cuts = 0, 0
        minExist = False
        for sw in sweetness:
            s += sw
            if s == minSweet:
                print("Found minSweet", s, minSweet, cuts)
                cuts += 1
                s = 0
                minExist = True
            elif s > minSweet:
                print("Found greater than minSweet", s, minSweet, cuts)
                cuts += 1
                s = 0
        print("cuts", cuts, "minExist", minExist, "canCut", cuts >= k and minExist)
        return cuts >= k and minExist