from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if len(triangle) == 1:
            return triangle[0][0]

        dp = [0] * len(triangle)
        dp[0] = triangle[0][0] + triangle[1][0]
        dp[1] = triangle[0][0] + triangle[1][1]

        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == len(triangle[i]) - 1:
                    dp[j] = triangle[i][j] + dp[j-1]
                elif j == 0:
                    dp[j] = triangle[i][j] + dp[j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
        return min(dp)

if __name__ == '__main__':
    s = Solution()
    triangle = [[-10]]
    ans = s.minimumTotal(triangle)
    print(ans)