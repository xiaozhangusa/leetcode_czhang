# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

# Thought process:
# 1. without using multiplication, division, and mod operator, then bit operation is the only way to go?
# 2.        

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # constants
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # handle extremes
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # convert both numbers to negative to avoid overflow
        negative = False
        if dividend > 0:
            dividend = -dividend
            negative = not negative
        if divisor > 0:
            divisor = -divisor
            negative = not negative
        
        # build an array of powers of two
        powerOfTwo = -1
        powersOfTwo, doubles = [], []
        while divisor >= dividend:
            powersOfTwo.append(powerOfTwo)
            doubles.append(divisor)
            powerOfTwo += powerOfTwo
            divisor += divisor
        
        # divide
        quotient = 0
        for i in reversed(range(len(powersOfTwo))):
            if doubles[i] >= dividend:
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
        
        # final check
        if negative:
            quotient = -quotient
        return quotient
                    
        
        
        
