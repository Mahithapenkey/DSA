class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            points,brainpower = questions[i]
            nidx= i+ brainpower + 1
            if nidx<n:
                npts= dp[nidx]
            else:
                npts=0
            
            dp[i] = max(points + npts,dp[i+1])
        return dp[0]
        