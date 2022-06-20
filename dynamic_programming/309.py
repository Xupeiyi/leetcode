from typing import List


class Solution1:
    def maxProfit(self, prices) -> int:
        dp = [[0, -prices[0], 0] for _ in range(len(prices))]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
        
        return max(dp[-1])


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nprices = len(prices)
        if nprices <= 1:
            return 0
        dp = [[0] * nprices for _ in range(2)]
        dp[0][0], dp[1][0] = -prices[0], 0
        dp[0][1], dp[1][1] = max(dp[1][0]-prices[1], dp[0][0]), max(dp[0][0]+prices[1], dp[1][0])

        for i in range(2, nprices):
            dp[0][i] = max(dp[1][i-2]-prices[i], dp[0][i-1])
            dp[1][i] = max(dp[0][i-1]+prices[i], dp[1][i-1])
        
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.maxProfit([1, 2, 3, 0, 2])
    print(ans)

