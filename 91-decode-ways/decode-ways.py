class Solution:
    def numDecodings(self, s: str) -> int:
        #dynamic programming

        # return 0 if the string starts with 0
        if not s or s[0] == '0':
            return 0

        # dp[i] stores the no of ways to decode the first i characters
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            # checking if the current digit can be decoded
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # check if the last two digits can be decoded
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
        