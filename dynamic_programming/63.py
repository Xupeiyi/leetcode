class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) if not obstacleGrid[i][j] else 0

        return dp[-1][-1]
        
        
if __name__ == '__main__':
    s = Solution()
    ans = s.uniquePathsWithObstacles([[1, 0]])
    print(ans)