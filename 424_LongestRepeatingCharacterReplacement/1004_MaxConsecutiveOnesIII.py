# 1004. Max Consecutive Ones III
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        freq = Counter()
        res = 0
        while end < len(nums):
            freq[nums[end]] += 1
            # shrink the window from the left if it has more than k distinct characters
            while freq[0] > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                start += 1
            res = max(res, end + 1 - start)
            end += 1
        return res
