class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1  # A single character needs only 1 print
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j] + 1  # Start with the assumption that it takes one more print
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
        
        return dp[0][n-1]
