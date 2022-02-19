class Solution:
    def permuteUnique(self, nums):
        ans = []
        
        def backtrack(rest, path):
            if not rest:
                ans.append(path)
                return
            
            used = set()
            for i in range(len(rest)):
                if rest[i] not in used:
                    used.add(rest[i])
                    backtrack(rest[:i] + rest[i+1:], path + [rest[i]])
        
        backtrack(nums, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.permuteUnique([1, 2, 3])
    print(ans)