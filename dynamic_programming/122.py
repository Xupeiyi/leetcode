class Solution1:
    def maxProfit(self, prices) -> int:
        dp = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                dp += diff
        return dp


from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in range(2)]
        dp[0][0] = -prices[0] 
        dp[1][0] = 0
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[1][i-1] - prices[i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1] + prices[i], dp[1][i-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(ans)