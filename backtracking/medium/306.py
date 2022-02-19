class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = False
        
        def backtrack(rest, path):
            nonlocal ans
            if not rest and len(path) > 2:
                ans = True
                return
            
            for i in range(0, len(rest)):
                n = int(rest[:i+1])
                
                if len(path) < 2 or n == path[-1] + path[-2]:
                    backtrack(rest[i+1:], path + [n])
                if n == 0:
                    break
        
        backtrack(num, [])
        return ans
 
   
if __name__ == '__main__':
    s = Solution()
    ans = s.isAdditiveNumber("199100199")
    print(ans)
    
    ans = s.isAdditiveNumber("112358")
    print(ans)