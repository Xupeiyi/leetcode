class Solution:
    def numTilings(self, n: int) -> int:
        to_state = {
            0: [3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 1, 2, 3],
        }
        
        dp = [[0]*len(to_state) for _ in range(n+1)]
        dp[1] = [1, 0, 0, 1]
        
        for i in range(2, n+1):
            for j in range(len(to_state)):
                dp[i][j] = sum(dp[i-1][k] for k in to_state[j])

        return dp[-1][3] % (10**9 + 7)
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.numTilings(1)
    print(ans)
    