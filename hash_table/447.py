from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        centers = defaultdict(int)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, n):
                x2, y2 = points[j][0], points[j][1]
                dist_sqr = (x2 - x1)**2 + (y2 - y1)**2
                centers[(x1, y1, dist_sqr)] += 1
                centers[(x2, y2, dist_sqr)] += 1
        return sum(n*(n-1) for n in centers.values())

if __name__ == '__main__':
    s = Solution()
    ans = s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
    print(ans)