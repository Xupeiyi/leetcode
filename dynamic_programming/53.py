from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [n for n in nums]

        for i, num in enumerate(nums[1:], start=1):
            if dp[i-1] < 0:
                dp[i] = num
            else:
                dp[i] = dp[i-1] + num
        return max(dp)
