class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr=len(grid)
        nc=len(grid[0])
        dp=[[0]*nc for _ in range(nr)]
        dp[0][0] = grid[0][0]
        #for row of dp updation
        for j in range(1,nc):
            dp[0][j]=grid[0][j]+dp[0][j-1]
        #for col of dp updation
        for i in range(1,nr):
            dp[i][0]=grid[i][0] +dp[i-1][0]

        for i in range(1,nr):
            for j in range(1,nc):
                dp[i][j] = grid[i][j] + min(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

        


        