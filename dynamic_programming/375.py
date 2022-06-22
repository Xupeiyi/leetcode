import math

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1) ]
        
        for k in range(2, n + 1):
            for start in range(1, n+2-k):
                end = start + k - 1
                dp[start][end] = math.inf
                for i in range(start, end+1):
                    amount = i
                    left = dp[start][i-1] if start <= i - 1 else 0
                    right = dp[i+1][end] if i + 1 <= end else 0
                    amount = amount + max(left, right)
                    dp[start][end] = min(amount, dp[start][end])
        return dp[1][-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.getMoneyAmount(12) 
    print(ans)
