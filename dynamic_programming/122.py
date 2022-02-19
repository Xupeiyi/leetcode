class Solution:
    def maxProfit(self, prices) -> int:
        dp = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                dp += diff
        return dp


if __name__ == '__main__':
    s = Solution()
    ans = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(ans)