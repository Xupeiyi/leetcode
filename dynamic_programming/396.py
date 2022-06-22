class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = sum(i * num for i, num in enumerate(nums))
        sum_ = sum(nums)
        for i in range(1, n):
            dp[i] = dp[i-1] + sum_ - n * nums[n-i]
        return max(dp)