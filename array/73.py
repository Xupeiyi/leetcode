def set_col_zero(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def set_row_zero(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row0_has_0 = any(map(lambda x: not bool(x), matrix[0]))
        col0_has_0 = any(map(lambda x: not bool(matrix[x][0]), range(m)))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                set_row_zero(matrix, i)
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                set_col_zero(matrix, j)

        if row0_has_0:
            set_row_zero(matrix, 0)
        
        if col0_has_0:
            set_col_zero(matrix, 0)
            
            
if __name__ == '__main__':
    s = Solution()
    mat = [[0, 1, 2, 0],
           [3, 4, 5, 2],
           [0, 3, 1, 5]]
    s.setZeroes(matrix=mat)
    print(*mat, sep='\n')
    
    