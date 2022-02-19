class Solution:
    def minPathSum(self, grid) -> int:
        h = len(grid[0])
        v = len(grid)
        
        dp = [[grid[i][j] for j in range(h)]
              for i in range(v)]
        
        for i in range(1, h):
            dp[0][i] += dp[0][i-1]
        
        for i in range(1, v):
            dp[i][0] += dp[i-1][0]
        
        for i in range(1, v):
            for j in range(1, h):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.minPathSum([[1, 3, 1],
                        [1, 5, 1],
                        [4, 2, 1]])
    print(ans)
