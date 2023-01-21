class Solution {
   
    
    List<Integer> list;
    int R=0;
    int C=0;
     public int maxAreaOfIsland(int[][] grid)  {
        R=grid.length;
        C=grid[0].length;
        list= new ArrayList<>();
        for(int r=0; r < R; r++){
            for(int c=0; c < C; c++){
                if(grid[r][c]==1)
                    
                    list.add(dfs(grid,r,c));
            }
        }
         int max=0;
        for(int i: list)
            max=Math.max(max,i);
        return max ;
    }
    public int dfs(int[][] grid, int r, int c){
        if(r<0 || r>=R || c>=C  || c<0 || grid[r][c]==0 )
            return 0;
         grid[r][c]=0;
        
        return 1+ dfs(grid,r-1,c)
        + dfs(grid,r+1,c)
        + dfs(grid,r,c-1)
        + dfs(grid,r,c+1);
    }
}