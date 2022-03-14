class Solution1:
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


class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2

            if mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        return end



if __name__ == '__main__':
    s = Solution()
    ans = s.mySqrt(25)
    print(ans)