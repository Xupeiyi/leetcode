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


class Solution:
    def searchMatrix(self, matrix, target: int):
        col0 = [row[0] for row in matrix]
        row_idx = bisect_right(col0, target) - 1
        if row_idx == -1:
            return False
        
        idx = bisect_right(matrix[row_idx], target) - 1
        if idx == -1 or matrix[row_idx][idx] != target:
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
    
    
    
    
    
    

