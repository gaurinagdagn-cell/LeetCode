class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #again initialize a 1d array 
        #solve using dynamic progamming

        #edge case: if the starting cell has an obstacle
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * n
        dp[0] = 1 
        
        for r in range(m):
            for c in range(n):
                #if an obstacle, no paths can pass through 
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    #curr dp[c] has the value from the row above
                    # dp[c-1] has the value from the left cell in the curr row
                    dp[c] += dp[c-1]
                    
        return dp[-1]

        