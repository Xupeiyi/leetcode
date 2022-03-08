from typing import List
from math import inf

def sum_range(start, end):
    return (start + end) * (end - start + 1) // 2


# 边界条件难以处理？手动设置极端值作为边界.
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums = [0] + nums + [inf]  # 如果不在两边加入最小值和最大值，逻辑会变得十分复杂
        diffs = [nums[i] - nums[i-1] - 1 for i in range(1, len(nums))]

        res = 0
        i = 0
        while k > 0:
            if diffs[i] > 0:
                res += sum_range(nums[i]+1, nums[i] + min(k, diffs[i]))
                k -= diffs[i]
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    ans = s.minimalKSum([4, 1, 25, 10, 25], 2)
    print(ans)
    ans = s.minimalKSum([5, 6], 6)
    print(ans)