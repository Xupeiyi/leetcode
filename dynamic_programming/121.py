class Solution:
    def maxProfit(self, prices) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
        return dp[-1]