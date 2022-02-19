class Solution0:
    def canPartition(self, nums):
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2
        
        dp = [nums[0] if j >= nums[0] else 0 for j in range(target+1)]
        
        for i, n in enumerate(nums[1:], start=1):
            for j in range(target, -1, -1):
                dp[j] = max(dp[j], dp[j-n] + n if j >= n else 0)
                if dp[j] == target:
                    return True
        return False


class Solution:
    def canPartition(self, nums):
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2

        if max(nums) > target:
            return False

        dp = [False for j in range(target)]
        dp[0] = True
        if nums[0] < target:
            dp[nums[0]] = True

        for i, n in enumerate(nums[1:], start=1):
            if dp[target-n]:
                return True
            for j in range(target-1, n-1, -1):
                dp[j] |= dp[j-n]
     
        return False

        
if __name__ == '__main__':
    s = Solution()
    ans = s.canPartition([1, 2, 5])
    print(ans)
    