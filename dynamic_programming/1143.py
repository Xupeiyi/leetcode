class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        
        dp = [[0] * l2 for _ in range(l1)]
        
        fill = 0
        for i in range(l1):
            if text1[i] == text2[0]:
                fill = 1
            dp[i][0] = fill
        
        fill = 0
        for j in range(l2):
            if text2[j] == text1[0]:
                fill = 1
            dp[0][j] = fill
        
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + int(text1[i] == text2[j]))
        
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

# ---------------------------
# 2022-06-08
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.longestCommonSubsequence("abcde", "ace")
    print(ans)