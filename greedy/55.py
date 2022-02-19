class Solution:
    def canJump(self, nums) -> bool:
        length = len(nums)
        
        i = 0
        furthest = 0
        while i <= furthest:
            furthest = max(i + nums[i], furthest)
            if furthest >= length - 1:
                return True
            i += 1
            
        return False


if __name__ == '__main__':
    s = Solution()
    ans = s.canJump([1, 1, 2, 0, 3, 0, 0, 0])
    print(ans)