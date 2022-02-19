class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        def rotatematrix(start, end):
            nonlocal matrix
            if start >= end:
                return
            for j in range(0, end-start):
                 matrix[start+j][end], matrix[end][end-j], matrix[end-j][start], matrix[start][start+j] = \
                    matrix[start][start+j], matrix[start+j][end], matrix[end][end-j], matrix[end-j][start]
        
            rotatematrix(start+1, end-1)
        
        rotatematrix(0, n-1)
    

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(*matrix, sep='\n')
    s.rotate(matrix)
    print('\n')
    print(*matrix, sep='\n')
