class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:  #negative power
            x = 1 / x
            n = -n

        result = 1

        while n:
            if n % 2 == 1:  #odd n cant be paired
                result *= x

            x *= x
            n //= 2 #even n sqaures base and halves exponent

        return result
        