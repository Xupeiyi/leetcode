class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0 for _ in range(4)] for p in prices]
        
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        
        for i, price in enumerate(prices[1:], 1):
            dp[i][0] = max(dp[i-1][0], -price)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + price)
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - price)
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + price)
            
        return dp[-1][-1]
    
        
if __name__ == '__main__':
    s = Solution()
    ans = s.maxProfit([3, 3, 5, 0, 0, 3, 1, 5])
    print(ans)