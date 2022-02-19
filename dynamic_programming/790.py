class Solution:
    def numTilings(self, n: int) -> int:
        to_state = {
            0: [3],
            1: [0, 2],
            2: [0, 1],
            3: [0, 1, 2, 3],
        }
        
        if n == 1 or n == 2:
            return n
        
        dp = [[0]*len(to_state) for _ in range(n+1)]
        dp[2] = [1, 1, 1, 2]
        
        for i in range(3, n+1):
            for j in range(len(to_state)):
                dp[i][j] = sum(dp[i-1][k] for k in to_state[j])

        return dp[-1][3] % (10**9 + 7)
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.numTilings(6)
    print(ans)
    