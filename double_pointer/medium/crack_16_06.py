from typing import List
import math


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        min_diff = math.inf
        while i < len(a) and j < len(b):
            
            while i < len(a) and a[i] <= b[j]:
                i += 1
            diff = min(a[i] - b[j], b[j] - a[i-1]) if i < len(a) else b[j] - a[i-1]
            min_diff = min(diff, min_diff)

            while i < len(a) and j < len(b) and a[i] > b[j]:
                j += 1
            if i < len(a):
                diff = min(b[j] - a[i], a[i] - b[j-1]) if j < len(b) else a[i] - b[j-1]
                min_diff = min(diff, min_diff)
        return min_diff

s = Solution()
ans = s.smallestDifference([6, 48], [5])
print(ans)