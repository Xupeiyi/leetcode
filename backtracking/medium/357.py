class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1, 9] + [0] * (n - 1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] * (9 + 2 - i)
        return sum(dp[:n+1])

if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(1))