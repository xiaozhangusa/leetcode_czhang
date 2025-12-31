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
        l, r = min(sweetness), sum(sweetness) // (k+1)
        while l < r:
            # !!!!!! Q: why need extra 1? Ans: because consider the case where left is already at the maximum workable value and right is the minimum unworkable value, 
            # We are only one step away from finishing the binary search. If we use mid = (left + right) / 2, we will get stuck in an infinite loop, as mid = left
            # acording to the rule for how we reduce the search space, l = mid, then [mid, right] = [left, right], which is the same as previous search space. 
            # However, using mid = (left + right + 1) / 2, since new mid is not workable, we will create new search space that [left, mid-1] = [left, right - 1] = [left, left], which can stop the loop.
            mid = (l + r + 1) // 2
            # inclusively
            if self.canCut(sweetness, mid, k):
                l = mid
            # exclusively
            else:
                # !!!! Q: why need less 1? Ans: this mid is not workable, so we need to exclude it.
                r = mid - 1
        return l
    
    def canCut(self, sweetness: List[int], maxMinSweet: int, k: int) -> bool:
        # print("new round")
        s, ppl = 0, 0
        minExist = False
        for sw in sweetness:
            s += sw
            if s >= maxMinSweet:
                ppl += 1
                s = 0
        # print("cuts", cuts, "minExist", minExist, "canCut:", cuts >= k and minExist)
        # return cuts >= k and minExist
        return ppl >= k+1