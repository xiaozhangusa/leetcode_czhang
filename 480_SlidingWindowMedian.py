import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians, window = [], []
        for i in range(len(nums)):
            if i >= k:
                window.remove(nums[i - k])
            bisect.insort(window, nums[i])
            
            if i >= k - 1:
                if k % 2 == 1:
                    median = float(window[k//2])
                else:
                    median = (window[k//2 - 1] + window[k//2]) / 2.0
                medians.append(median)
        return medians
        