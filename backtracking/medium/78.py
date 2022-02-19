
class Solution:
    def subsets(self, nums):
        ans = []
        
        def backtrack(rest, path):
            if not rest:
                ans.append(path)
                return
            
            backtrack(rest[1:], path+[rest[0]])
            backtrack(rest[1:], path)
        
        backtrack(nums, [])
        return ans
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.subsets([1, 2, 3])
    print(ans)
    
