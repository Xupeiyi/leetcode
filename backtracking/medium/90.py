class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        if not nums:
            return ans
        
        def backtrack(rest, abandoned, path):
            if not rest:
                ans.append(path)
                return
            
            if rest[0] not in abandoned:
                backtrack(rest[1:], abandoned, path + [rest[0]])
            backtrack(rest[1:], abandoned | {rest[0]}, path)
            
        backtrack(nums, set(), [])
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.subsetsWithDup([1, 2, 2])
    print(ans)