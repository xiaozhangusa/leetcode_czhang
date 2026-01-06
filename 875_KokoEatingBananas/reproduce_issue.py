
from typing import List

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
        s, cuts = 0, 0
        minExist = False
        for sw in sweetness:
            s += sw
            if s == minSweet:
                cuts += 1
                s = 0
                minExist = True
            elif s > minSweet:
                cuts += 1
                s = 0
        return cuts >= k and minExist

def test():
    sol = Solution()
    
    # Example 1
    sweetness1, k1 = [1,2,3,4,5,6,7,8,9], 5
    res1 = sol.maximizeSweetness(sweetness1, k1)
    print(f"Test 1: sweetness={sweetness1}, k={k1}")
    print(f"Expected: 6, Got: {res1}")
    
    # Example 2
    sweetness2, k2 = [5,6,7,8,9,1,2,3,4], 8
    res2 = sol.maximizeSweetness(sweetness2, k2)
    print(f"Test 2: sweetness={sweetness2}, k={k2}")
    print(f"Expected: 1, Got: {res2}")
    
    # Example 3
    sweetness3, k3 = [1,2,2,1,2,2,1,2,2], 2
    res3 = sol.maximizeSweetness(sweetness3, k3)
    print(f"Test 3: sweetness={sweetness3}, k={k3}")
    print(f"Expected: 5, Got: {res3}")

if __name__ == "__main__":
    test()
