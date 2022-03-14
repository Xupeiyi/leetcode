def bisect_right(sequence, x):
    hi = len(sequence) - 1
    lo = 0
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if sequence[mid] == x:
            return mid + 1
        
        elif sequence[mid] < x:
            lo = mid + 1
        
        else:
            hi = mid - 1
    
    return lo


class Solution1:
    def searchMatrix(self, matrix, target: int):
        col0 = [row[0] for row in matrix]
        row_idx = bisect_right(col0, target) - 1
        if row_idx == -1:
            return False
        
        idx = bisect_right(matrix[row_idx], target) - 1
        if idx == -1 or matrix[row_idx][idx] != target:
            return False
        
        return True

# 返回最大的小于等于target的元素idx
def bisect_rightmost(nums, target):
    
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return end


class Solution:
    def searchMatrix(self, matrix, target: int):
        col0 = [row[0] for row in matrix]
        row_idx = bisect_rightmost(col0, target)
        if row_idx == -1:
            return False
            
        col_idx = bisect_rightmost(matrix[row_idx], target)
        if col_idx == -1 or matrix[row_idx][col_idx] != target:
            return False
        
        return True

        
        

if __name__ == '__main__':
    # print(bisect_right([0, 1, 3, 5, 7], -1) == 0)
    # print(bisect_right([0, 1, 3, 4, 5], 0) == 1)
    # print(bisect_right([0, 1, 3, 4, 5], 5) == 5)
    # print(bisect_right([0, 1, 3, 4, 5], 6) == 5)
    # print(bisect_right([0, 1, 3, 4, 5], 4) == 4)
    # print(bisect_right([0, 1, 3, 4, 5], 1) == 2)
    
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

    ans = s.searchMatrix(matrix, 3)
    print(ans)
    
    ans = s.searchMatrix(matrix, 20)
    print(ans)
    
    
    
    
    
    

