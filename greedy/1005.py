# ---------------------
# Solution1
class Solution0:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        while k > 0:
            i = min(range(len(nums)), key=lambda x:nums[x])
            nums[i] *= -1
            k -= 1
            
        return sum(nums)

# ----------------------
# Solution2

class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)  # 将A按绝对值从大到小排列
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= (-1) ** k  # 取A最后一个数只需要写-1
        return sum(nums)


if __name__ == '__main__':
    s = Solution()
    ans = s.largestSumAfterKNegations([4, 2, 3], 1)
    print(ans)