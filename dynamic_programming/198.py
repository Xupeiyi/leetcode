class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])] + [0] * (len(nums) - 2)
        for i, num in enumerate(nums[2:], 2):
            dp[i] = max(dp[i-1], dp[i-2] + num)
        
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.rob([2])
    print(ans)
    