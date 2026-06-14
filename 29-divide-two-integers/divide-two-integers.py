class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        #overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        #if result should be negative
        sign = (dividend < 0) ^ (divisor < 0)

        #positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            curr = divisor
            count = 1

            #doubling the divisor until it is > dividend
            while dividend >= (curr << 1):
                curr <<= 1
                count <<= 1

            dividend -= curr
            quotient += count

        # sign
        return -quotient if sign else quotient