# 一开始的思路：
#       v v            (v 指向要与2, 3, 5相乘的丑数) 
#   1 2 3 4 5 6  
# 2 T T T
# 3 T T   T  
# 5 T T T              (使用过的丑数和因子标记为True)

# 其实 V 应该有三个才对（不然无法推广到5）。这样就和题解思路相同了。但题解显然简洁不少。
class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n+1):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                p2 += 1
            if dp[i] == n3:
                p3 += 1
            if dp[i] == n5:
                p5 += 1
        
        return dp[n]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[p2] * 2 == dp[i]:
                p2 += 1
            if dp[p3] * 3 == dp[i]:
                p3 += 1
            if dp[p5] * 5 == dp[i]:
                p5 += 1
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.nthUglyNumber(10)
    print(ans)