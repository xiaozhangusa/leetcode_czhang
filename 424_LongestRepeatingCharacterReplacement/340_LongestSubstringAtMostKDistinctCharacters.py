
# Code
# Testcase
# Testcase
# Test Result
# 340. Longest Substring with At Most K Distinct Characters
# Medium
# Topics
# conpanies icon
# Companies
# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lo, hi = k, len(s) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.isValid(s, mid, k):
                lo = mid
            else:
                hi = mid
        return hi

    def isValid(self, s: str, sublen: int, k: int) -> bool:
        # slide window of size sublen
        # check if it has at most k distinct characters
        # if so, return True
        # else, return False
        # freq = Counter(s[:sublen])
        # if len(freq) <= k:
        #     return True
        print("this round sublen: ", sublen)
        freq = {}
        start = 0
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            print("substr: ", s[start:end+1])
            if end - start == sublen and len(freq) <= k:
                return True
            if end + 1 - start > sublen:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
        return False
