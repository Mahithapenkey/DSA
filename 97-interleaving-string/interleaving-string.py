class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        if l1+l2 !=len(s3):
            return False
        dp=[[False]*(l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        for row in range(l2+1):
            for col in range(l1+1):
                if col > 0 and dp[row][col-1] and s1[col-1] == s3 [row+col-1]:
                    dp[row][col]=True
                if row >0 and dp[row-1][col] and s2[row-1] == s3[row+col-1]:
                    dp[row][col]= True
        return dp[-1][-1]
                
