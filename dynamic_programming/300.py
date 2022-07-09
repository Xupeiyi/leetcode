from typing import List

class Solution:
    def lengthOfLIS(self, nums) -> int:
        
        dp = [1] * len(nums)
        
        res = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > res:
                res = dp[i]
        return res


# --------------------------------
# 2022-06-08
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    ans = s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print(ans)
