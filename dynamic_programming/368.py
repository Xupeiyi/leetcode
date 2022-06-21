from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [[] for _ in nums]

        for i, num in enumerate(nums):
            for j in range(i-1, -1, -1):
                if num % nums[j] == 0 and len(dp[i]) < len(dp[j]):
                    dp[i] = [n for n in dp[j]]
            dp[i] += [num]
        return max(dp, key=len)

if __name__ == '__main__':
    s = Solution()
    ans = s.largestDivisibleSubset([4, 8, 10, 240])
    print(ans)