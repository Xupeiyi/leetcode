class Solution:
    def coinChange(self, coins, amount: int):
        dp = [0] * (amount + 1)
        
        for i in range(1, amount+1):
            nums = [dp[i-c]+1 for c in coins if i >= c and dp[i-c] != -1]
            dp[i] = min(nums) if nums else -1
            
        return dp[-1]
    
    
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
    