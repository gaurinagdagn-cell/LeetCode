class Solution:
    def numTrees(self, n: int) -> int:
        #dynamic programming

        # stores the no of unique bst's with i nodes
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        # calculate the no of trees for each no of nodes
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # multiply the number of left and right subtrees
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
        