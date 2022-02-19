class Solution:
    def permute(self, nums):
        ans = []
        
        def backtrack(rest, path):
            if not rest:
                ans.append(path)
                return
            
            for i in range(len(rest)):
                backtrack(rest[:i] + rest[i+1:], path + [rest[i]])
        
        backtrack(nums, [])
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.permute([])
    print(ans)
    