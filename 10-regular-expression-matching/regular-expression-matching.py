class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dynamic progamming
        m, n = len(s), len(p)

        # dp[i][j] = true if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # empty string 
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # filling the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # curr chars match or pattern has '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]

                # pattern contains '*'
                elif p[j - 1] == "*":
                    # match 0 occurrences of prev char
                    dp[i][j] = dp[i][j - 2]

                    # match one or more occurr
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]