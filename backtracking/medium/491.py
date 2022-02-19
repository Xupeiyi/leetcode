

class Solution:
    def findSubsequences(self, nums):
        ans = []
        
        def backtrack(rest, path):
            
            if len(path) >= 2:
                ans.append(path)
            
            if not rest:
                return
            
            used = set()
            for i, num in enumerate(rest):
                if num not in used and (not len(path) or num >= path[-1]):
                    used.add(num)
                    backtrack(rest[i+1:], path + [num])
        
        backtrack(nums, [])
        return ans
        

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 1]
    ans = s.findSubsequences(nums)
    print(ans)
