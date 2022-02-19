class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [1] + [0] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[-1]
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.change(8, [2, 3, 5])
    print(ans)