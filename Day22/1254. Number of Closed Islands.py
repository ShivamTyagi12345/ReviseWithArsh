class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C, count=  len(grid), len(grid[0]), 0
        def dfs(r,c):
            if r not in range(R) or c not in range(C) or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        for r in range(R):
            if grid[r][0]==0:
                dfs(r,0)
            if grid[r][C-1]==0:
                dfs(r,C-1)


    
        for c in range(C):
                if grid[0][c]==0:
                    dfs(0,c)
                if grid[R-1][c]==0:
                    dfs(R-1,c)

        for r in range(1,R):
            for c in range(1,C):
                if grid[r][c]==0:
                    dfs(r,c)
                    count +=1


        
        return count
        

                