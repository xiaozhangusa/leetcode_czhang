# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        vowels = [ 'a', 'e', 'i', 'o', 'u']
        res = list(s)
        round = 0
        while True:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            # now both l and r should be vowels
            print("round: ", round)
            print ("l and r: ", l, res[l], r, res[r])
            if l < r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            else:
                break
        return "".join(res)
