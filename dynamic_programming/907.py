# from typing import List

# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         n = len(arr)
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = arr[i]

#         ans = sum(arr)
#         for length in range(2, n + 1):
#             for start in range(0, n - length + 1):
#                 end = start + length - 1
#                 dp[start][end] = min(dp[start][end-1], dp[start+1][end])
#                 ans += dp[start][end]
#         return ans

# if __name__ == '__main__':
#     s = Solution()
#     ans = s.sumSubarrayMins([11, 81, 94, 43, 3])
#     print(ans)