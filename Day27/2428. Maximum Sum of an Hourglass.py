class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R, C= len(grid)-2, len(grid[0])-2 #R= 2, C= 2
        res = 0

        def helper(r, c):
            return grid[r][c]+ grid[r][c+1] + grid[r][c+2] + grid[r+1][c+1]+ grid[r+2][c]+ grid[r+2][c+1]+grid[r+2][c+2]
        for r in range(R):
            for c in range(C):
                res = max(res, helper(r, c))
        return res