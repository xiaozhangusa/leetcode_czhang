class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return 1
        len_digits = len(digits)
        carry = 0
        for i in range(len_digits-1, -1, -1):
            print digits[i]
            if i == len_digits-1:
                tmp = digits[i] + 1
            else:
                tmp = digits[i] + carry
            rem = tmp % 10
            carry = tmp / 10
            digits[i] = rem
        if carry > 0:
            digits = [1] + digits
        return digits

digits = [1, 0]
sol = Solution()
res = sol.plusOne(digits)
print res