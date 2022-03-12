from re import S
from typing import List
from math import inf

def gen_coverage(arr, start, end):
    if start == end:
        return f"{arr[start]}"
    else:
        return f"{arr[start]}->{arr[end]}"


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        nums += [inf]
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                coverage = gen_coverage(nums, start, i-1)
                res.append(coverage)
                start = i
        return res

if __name__ == '__main__':
    s = Solution()
    ans = s.summaryRanges([0,2,3,4,6,8,9])
    print(ans)