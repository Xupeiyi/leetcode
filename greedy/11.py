class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        
        max_area = 0
        while i < j:
            min_idx = i if height[i] <= height[j] else j
            area = (j - i) * height[min_idx]
            
            if area > max_area:
                max_area = area
            
            if min_idx == i:
                i += 1
            elif min_idx == j:
                j -= 1
        
        return max_area


if __name__ == '__main__':
    s = Solution()
    ans = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(ans == 49)
    
    ans = s.maxArea([1, 1])
    print(ans == 1)
    
    ans = s.maxArea([4, 3, 2, 1, 4])
    print(ans == 16)
    
    ans = s.maxArea([1, 2, 1000, 10000, 3, 1])
    print(ans == 1000)