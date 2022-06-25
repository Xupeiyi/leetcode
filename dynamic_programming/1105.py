from typing import List
import math

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            width, height = 0, 0
            for j in range(i, -1, -1):
                width += books[j][0]
                if width > shelf_width:
                    break
                height = max(height, books[j][1])
                dp[i+1] = min(dp[i+1], dp[j] + height)
                
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    ans = s.minHeightShelves(books, 4)
    print(ans)
