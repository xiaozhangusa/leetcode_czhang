# Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

# Implement the StringIterator class:

# next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
# hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
 

# Example 1:

# Input
# ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
# [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
# Output
# [null, "L", "e", "e", "t", "C", "o", true, "d", true]

# Explanation
# StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
# stringIterator.next(); // return "L"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "t"
# stringIterator.next(); // return "C"
# stringIterator.next(); // return "o"
# stringIterator.hasNext(); // return True
# stringIterator.next(); // return "d"
# stringIterator.hasNext(); // return True
 

# Constraints:

# 1 <= compressedString.length <= 1000
# compressedString consists of lower-case an upper-case English letters and digits.
# The number of a single character repetitions in compressedString is in the range [1, 10^9]
# # At most 100 calls will be made to next and hasNext.

import re

class StringIterator:

    def __init__(self, compressedString: str):
        # Find all character-number pairs. e.g., "a2b1" -> [('a', '2'), ('b', '1')]
        self.tokens = re.findall(r'([a-zA-Z])(\d+)', compressedString)
        self.cursor = 0  # Index of the current token
        if self.tokens:
            self.current_char = self.tokens[0][0]
            self.remaining_count = int(self.tokens[0][1])
        else:
            self.current_char = ''
            self.remaining_count = 0

    def next(self) -> str:
        # hasNext() acts as a guard. If remaining_count is 0, we never reach the decrement logic.
        if not self.hasNext():
            return ' '
        
        res = self.current_char
        self.remaining_count -= 1
        
        # If the current group is exhausted, proactively move to the next one
        if self.remaining_count == 0:
            self.cursor += 1
            if self.cursor < len(self.tokens):
                self.current_char = self.tokens[self.cursor][0]
                self.remaining_count = int(self.tokens[self.cursor][1])
            else:
                self.current_char = '' # Signal that we are truly empty
                
        return res

    def hasNext(self) -> bool:
        # Since next() proactively updates remaining_count to the next group,
        # this single check is all we need.
        return self.remaining_count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()