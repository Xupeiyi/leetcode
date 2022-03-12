from typing import List
import math

# 排序能够帮助划分边界。                 index   1  2  3  4  5
# 比如对 citations = [3, 0, 6, 1, 5]， 排序后为 [6, 5, 3, 1, 0]
# index i 隐含地表示了引用量大于等于citations[i]的数量
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        citations = [math.inf] + citations + [-math.inf]
        for i, citation in enumerate(citations[:-1]):
            if citation >= i and citations[i+1] <= i:
                return i
        return 0

if __name__ == '__main__':
    s = Solution()
    ans = s.hIndex([3, 0, 6, 1, 5])
    print(ans)