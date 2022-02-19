class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        start = 1
        end = x
        
        while start <= end:
            mid = (start + end) // 2
            mid_square = mid*mid
            mid1_square = (mid+1)*(mid+1)
            
            if mid_square <= x <= mid1_square:
                return mid + int(mid1_square == x)
            
            elif mid_square > x:
                end = mid - 1
            
            elif mid1_square < x:
                start = mid + 1

    
if __name__ == '__main__':
    s = Solution()
    for i in range(1000):
        ans = s.mySqrt(i)
        print(ans)