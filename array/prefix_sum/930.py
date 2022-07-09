from typing import List
from itertools import accumulate

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0] + list(accumulate(nums))

        start, end = 0, 0
        cnt = 0

        for i, pref in enumerate(prefix, start=1):
            while start < i and pref - prefix[start] > goal:
                start += 1

            if end < start:
                end = start
            
            if pref - prefix[start] == goal:
                while end < i and prefix[end] == prefix[start]:
                    end += 1
                cnt += (end - start)

        return cnt

if __name__ == '__main__':
    s = Solution()
    ans = s.numSubarraysWithSum([0, 0, 0, 0, 0], 0)
    print(ans == 15)

    ans = s.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
    print(ans == 4)
