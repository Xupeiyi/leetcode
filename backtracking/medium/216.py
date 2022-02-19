class Solution:
    def combinationSum3(self, k: int, n: int):
        ans = []
        
        def backtrack(curr, remain, usable, path):
            if remain == 0:
                ans.append(path)
                return
            
            if usable == 0:
                return
            
            start = max(curr+1, int(remain - (20 - usable) * (usable - 1) / 2))
            end = min(9, int(1/2*(2*remain/usable-usable+1)), 9-usable+1)
            for num in range(start, end+1):
                backtrack(num, remain-num, usable-1, path+[num])
            
        backtrack(0, n, k, [])
        return ans
 
    
if __name__ == '__main__':
    s = Solution()
    ans = s.combinationSum3(3, 20)
    print(ans)