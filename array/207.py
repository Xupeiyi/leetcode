class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        length = len(nums)
        sub_len = length + 1
        i = 0
        sum_ = 0
        for j in range(0, length):
            sum_ += nums[j]
            while sum_ - nums[i] >= target:
                sum_ -= nums[i]
                i += 1
            if sum_ >= target:
                sub_len = min(sub_len, j - i + 1)
        
        return sub_len if sub_len <= length else 0
        
        
if __name__ == '__main__':
    s = Solution()
    n = [1, 1, 1, 1, 1, 1, 1]
    print(s.minSubArrayLen(7, n))