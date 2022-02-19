class Solution:
    def findLength(self, nums1, nums2) -> int:
        l1, l2 = len(nums1), len(nums2)
        
        dp = [[0] * l2 for _ in range(l1)]
        
        fill = 0
        for i in range(l1):
            if nums1[i] == nums2[0]:
                fill = 1
            dp[0][i] = fill
        
        fill = 0
        for j in range(l2):
            if nums2[j] == nums1[0]:
                fill = 1
            dp[j][0] = fill
        
        res = 0
        for j in range(1, l2):
            for i in range(1, l1):
                if nums2[j] == nums1[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]
                
        return res
        

if __name__ == '__main__':
    s = Solution()
    ans = s.findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1])
    print(ans)