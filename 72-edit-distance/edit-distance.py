class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        #if word2 is empty delete all characters of word1
        for i in range(m + 1):
            dp[i][n] = m - i

        #if word1 is empty  insert all characters of word2
        for j in range(n + 1):
            dp[m][j] = n - j

        #filling table from bottom right to top left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j + 1],     #insert
                        dp[i + 1][j],     #delete
                        dp[i + 1][j + 1]  #replace
                    )

        return dp[0][0]
        