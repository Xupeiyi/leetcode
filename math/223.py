class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        w1, h1 = ax2 - ax1, ay2 - ay1
        w2, h2 = bx2 - bx1, by2 - by1
        overlapped = (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1)) \
                     if not (bx2 < ax1 or bx1 > ax2 or by2 < ay1 or by1 > ay2) \
                     else 0
        return w1 * h1 + w2 * h2 - overlapped


if __name__ == '__main__':
    s = Solution()
    ans = s.computeArea(-5, -5, 0, -4, -3, -3, 3, 3)
    print(ans)