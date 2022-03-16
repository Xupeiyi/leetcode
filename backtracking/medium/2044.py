from typing import List
from functools import reduce


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)
        cnt = 0
        length = len(nums)

        def backtrack(idx, curr_or):
            nonlocal max_or, cnt, length
            if idx == length:
                return

            new_or = nums[idx] | curr_or
            if new_or == max_or:
                cnt += 1
            backtrack(idx + 1, new_or)
            backtrack(idx+1, curr_or)

        backtrack(0, 0)
        return cnt

if __name__ == '__main__':
    s = Solution()
    ans = s.countMaxOrSubsets([2,2,2])
    print(ans)