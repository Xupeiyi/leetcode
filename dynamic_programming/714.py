from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        nprices = len(prices)
        dp = [[0] * nprices for _ in range(2)]
        dp[0][0] = -prices[0]
        dp[1][0] = 0

        for i in range(1, nprices):
            dp[0][i] = max(dp[1][i-1]-prices[i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1]+prices[i]-fee, dp[1][i-1])
        
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    s.maxProfit([])