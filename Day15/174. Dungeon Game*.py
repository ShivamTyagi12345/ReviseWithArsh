class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # the minimum life needed to survive to the finish point
        m = len(dungeon)
        n = len(dungeon[0])
        dp = dungeon

        dp[m-1][n-1] = max(1, -dp[m-1][n-1]+1)

        for i in range(n-2, -1, -1):
            dp[m-1][i] = max(1, -dp[m-1][i] + dp[m-1][i+1])
        for j in range(m-2, -1, -1):
            dp[j][n-1] = max(1, -dp[j][n-1] + dp[j+1][n-1]) 
 
        for j in range(m-2, -1, -1):
            for i in range(n-2, -1, -1):
                dp[j][i] = max(1, -dp[j][i] + min(dp[j+1][i], dp[j][i+1]))
        
        return dp[0][0]




            