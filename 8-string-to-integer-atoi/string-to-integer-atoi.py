class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        result = 0

        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        for char in s:
            if not char.isdigit():
                break

            digit = int(char)

            # Overflow check
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit

        return sign * result