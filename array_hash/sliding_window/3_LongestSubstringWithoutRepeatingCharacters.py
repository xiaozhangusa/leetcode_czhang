# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Store the last seen index of each character
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If the character is already in the map and within the current window
            if char in char_map and char_map[char] >= left:
                # Move the 'left' pointer to one position after the last seen index
                left = char_map[char] + 1
            
            # Update the last seen index of the character
            char_map[char] = right
            # Calculate the window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length