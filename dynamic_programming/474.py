def count01(s):
    zero, one = 0, 0
    for c in s:
        if c == '0':
            zero += 1
        elif c == '1':
            one += 1
    return zero, one


class Solution:
    def findMaxForm(self, strs, m: int, n: int):
        zos = list(map(count01, strs))
        
        zero0, one0 = count01(strs[0])
        dp = [[1 if (i >= zero0 and j >= one0) else 0 for j in range(n+1)]
              for i in range(m+1)]
        
        for s in strs[1:]:
            zero, one = count01(s)
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i-zero][j-one] + 1, dp[i][j])
                    
        # for r in dp:
        #     print(r)
        return dp[-1][-1]

        

if __name__ == '__main__':
    s = Solution()
    ans = s.findMaxForm(strs=["10", "1", "0"], m=1, n=1)
    print(ans)
    