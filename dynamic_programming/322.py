class Solution:
    def coinChange(self, coins, amount: int):
        dp = [0] * (amount + 1)
        
        for i in range(1, amount+1):
            nums = [dp[i-c]+1 for c in coins if i >= c and dp[i-c] != -1]
            dp[i] = min(nums) if nums else -1
            
        return dp[-1]
    
    
# ------------------------------
# 2022-06-08
from math import inf
class Solution:
    def coinChange(self, coins, amount):
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >=0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != inf else -1



if __name__ == '__main__':
    s = Solution()
    ans = s.coinChange([1, 2, 5], 11)
    print(ans)
    
    ans = s.coinChange([2], 3)
    print(ans)
    
    ans = s.coinChange([1], 0)
    print(ans)
    
    ans = s.coinChange([1], 1)
    print(ans)

    ans = s.coinChange([1], 2)
    print(ans)
    