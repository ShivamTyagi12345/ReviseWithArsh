class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {}
        # it has to be on the board after k moves
        
        def helper(r, c, steps):
            if not 0<=r<n or not 0<= c <n:
                return 0
            if steps == 0:
                return 1
            if (r, c, steps) in dp:
                # print dp[r, c, steps]
                return dp[(r, c, steps)]
            ans = 0
            for u, v in [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]: 
                ans+= helper(u, v, steps-1)/8
            dp[(r, c, steps)] = ans
            return ans
        return helper(row, column, k) 




            
