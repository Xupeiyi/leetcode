from typing import List


# 矩阵的起点并不一定总是在左上角
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])

        i, j = 0, ncols - 1
        while i < nrows and j >= 0:

            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
            