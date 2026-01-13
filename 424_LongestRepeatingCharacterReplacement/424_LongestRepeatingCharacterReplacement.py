# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo, hi = 1, len(s) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            # inclusive
            if self.canReplace(s, mid, k):
                lo = mid
            else:
                hi = mid
        return lo


    def canReplace(self, s: str, sublen: int, k: int) -> bool:
        start = 0
        freq = {}
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            # slide window to the right by 1, shrink window from the left by 1
            if end + 1 - start > sublen:
                freq[s[start]] -= 1
                start += 1
            maxFreq = max(freq.values())
            # if the number of replacements needed is less than or equal to k, return true
            if sublen - maxFreq <= k:
                return True
        return False