class Solution0:
    def findTargetSumWays(self, nums, target: int):
        num_sum = sum(nums)
        if target > num_sum or target < -num_sum:
            return 0
        
        new_target = target + num_sum
        new_nums = [2*n for n in nums]
        dp = [0] * (new_target+1)
        dp[0] += 1
        if new_nums[0] <= new_target:
            dp[new_nums[0]] += 1

        for n in new_nums[1:]:
            for i in range(new_target, n-1, -1):
                dp[i] += dp[i-n]

        return dp[-1]


class Solution:
    def findTargetSumWays(self, nums, target: int):
        num_sum = sum(nums)
        if target > num_sum or target < -num_sum:
            return 0
        
        new_target = num_sum - target
        if new_target % 2 != 0:
            return 0
        new_target = new_target // 2
        
        dp = [0] * (new_target+1)
        dp[0] += 1
        if nums[0] <= new_target:
            dp[nums[0]] += 1

        for n in nums[1:]:
            for i in range(new_target, n-1, -1):
                dp[i] += dp[i-n]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.findTargetSumWays([3, 2, 5, 6, 9], 3)
    # ans = s.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)
    print(ans)