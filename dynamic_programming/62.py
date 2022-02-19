class Solution:
    def uniquePaths(self, m: int, n: int):
        dp = [[int(i == 0 or j == 0) for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
    

if __name__ == '__main__':
    s = Solution()
    ans = s.uniquePaths(3, 3)
    print(ans)