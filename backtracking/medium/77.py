class Solution:
    def combine(self, n: int, k: int):
        ans = []
        
        def backtrack(curr, remain, path):
            nonlocal ans
            if remain == 0:
                ans.append(path)
                return
            
            for num in range(curr+1, n-remain+2):
                backtrack(num, remain-1, path + [num])
        
        backtrack(0, k, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    
    ans = s.combine(4, 3)
    print(ans)
    

