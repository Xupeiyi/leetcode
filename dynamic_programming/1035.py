class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        