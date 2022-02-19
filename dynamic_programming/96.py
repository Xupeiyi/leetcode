class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0] * (n-1)
        
        for i in range(2, n+1):
            trees = 0
            for root in range(1, i+1):
                left_num = root - 1
                right_num = i - root
                trees += dp[left_num] * dp[right_num]
            dp[i] = trees
            
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    ans = s.numTrees(3)
    print(ans)