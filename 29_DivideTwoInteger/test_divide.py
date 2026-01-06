
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

sol = Solution()
dividend = 10
divisor = 3
result = sol.divide(dividend, divisor)
print(f"Dividend: {dividend}, Divisor: {divisor}")
print(f"Result: {result}")
