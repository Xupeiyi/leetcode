class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[0, -prices[0], 0] for _ in range(len(prices))]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
        
        return max(dp[-1])

        