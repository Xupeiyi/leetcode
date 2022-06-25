from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0 for _ in nums]
        dp[2] = int((nums[2] - nums[1]) == (nums[1] - nums[0]))       
        for i in range(3, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
