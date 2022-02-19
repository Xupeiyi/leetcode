class Solution:
    def wiggleMaxLength(self, nums) -> int:
        pre_diff = 0
        res = 1  # 题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff * pre_diff <= 0 and diff != 0:  # 差值为0时，不算摆动
                res += 1
                pre_diff = diff  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return res


if __name__ == '__main__':
    s = Solution()
    ans = s.wiggleMaxLength([3, 3, 3, 2, 5])
    print(ans)
