class Solution:
    def numSquares(self, n: int) -> int:
        
        sqrs = []
        start = 1
        sqr = 1
        while sqr <= n:
            sqrs.append(sqr)
            start += 1
            sqr = start**2
        
        if sqrs[-1] == n:
            return 1

        dp = [0] + [i for i in range(1, n+1)]

        for sqr in sqrs[1:]:
            for i in range(sqr, n+1):
                dp[i] = min(dp[i], dp[i-sqr]+1)
        
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    ans = s.numSquares(13)
    print(ans)