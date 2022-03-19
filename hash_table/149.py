from typing import List
from math import inf
from collections import defaultdict


def gcd(a, b):
        return a if b == 0 else gcd(b, a % b) 


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        npoints= len(points)
        if npoints == 1:
            return 1

        max_points = 0
        for i in range(npoints-1):
            tangents = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i+1, npoints):
                x2, y2 = points[j]
                a, b = y2 - y1, x2 - x1
                n = gcd(a, b)
                k = (a // n, b // n) 
                tangents[k] += 1
            max_points = max(max(tangents.values()), max_points)
        return max_points + 1


if __name__ == '__main__':
    s = Solution()
    ans = s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    print(ans)