from typing import List

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Partition a string into all possible sets of palindromic substrings.
        
        Approach: Backtracking (DFS)
        The idea is to split the string into a prefix and a suffix. If the prefix 
        is a palindrome, we recursively partition the remaining suffix.
        
        Example Trace for s = "aab":
        1. DFS("aab", [])
           - i=1: "a" is pal. -> DFS("ab", ["a"])
             - i=1: "a" is pal. -> DFS("b", ["a", "a"])
               - i=1: "b" is pal. -> DFS("", ["a", "a", "b"])
                 - Found: ["a", "a", "b"]
             - i=2: "ab" not pal.
           - i=2: "aa" is pal. -> DFS("b", ["aa"])
             - i=1: "b" is pal. -> DFS("", ["aa", "b"])
               - Found: ["aa", "b"]
           - i=3: "aab" not pal.
        
        Result: [["a", "a", "b"], ["aa", "b"]]
        """
        result = []
        # Start depth-first search from the beginning of the string
        self.dfs(s, [], result)
        return result

    def isPalindrome(self, s: str) -> bool:
        """Helper to check if a string is a palindrome."""
        return s == s[::-1]

    def dfs(self, s: str, path: List[str], result: List[List[str]]):
        # Base Case: If the remaining string is empty, we've found a valid partition
        if not s:
            result.append(path)
            return
        
        # Try every possible split point from the start of the current string 's'
        # i represents the length of the prefix we are currently checking
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            # If the prefix is a palindrome, recurse on the remaining suffix
            if self.isPalindrome(prefix):
                # path + [prefix] creates a NEW list, which implicitly handles backtracking
                # for us (it doesn't modify the 'path' variable in the current frame)
                self.dfs(s[i:], path + [prefix], result)