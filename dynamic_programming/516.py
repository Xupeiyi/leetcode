class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[1] * len(s) for _ in s]
        
        for k in range(1, len(s)+1):
            for i in range(0, len(s)-1):
                j = i + k
                if j >= len(s):
                    break

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1] if k > 1 else 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        
        for k in range(2, length + 1):
            for i in range(length-k + 1):
                j = i + k - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.longestPalindromeSubseq("bbbab")
    print(ans)