from typing import List
from math import inf

# 二分查找的难点在于选择哪一边进行查找
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.insert(0, -inf)
        n = len(citations)
        start, end = 1, n-1

        while start <= end:
            mid = (start + end) // 2

            npapers = n - mid
            if npapers <= citations[mid] and citations[mid-1] <= npapers:
                return npapers

            elif npapers > citations[mid]:
                start = mid + 1
            
            elif citations[mid-1] > npapers:
                end = mid - 1
        
        return 0
if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([1]))
        