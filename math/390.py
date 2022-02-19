class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 0
        l_to_r = True
        
        first = 1
        while n > 1:
            
            if l_to_r or (not l_to_r and n % 2 == 1):
                first += 2**step
            
            l_to_r = not l_to_r
            step += 1
            n = n//2
        
        return first
    
    
if __name__ == '__main__':
    s = Solution()
    ans = s.lastRemaining(22)
    print(ans)
    