class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [1] + [0] * target
        
        for i in range(target+1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i-n]
        
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.combinationSum4([9], 3)
    print(ans)