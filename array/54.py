class Solution:
    def spiralOrder(self, matrix):

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []
        while True:
            for l in range(left, right + 1):
                ans.append(matrix[top][l])
            top += 1
            if top > bottom:
                break
            
            for t in range(top, bottom + 1):
                ans.append(matrix[t][right])
            right -= 1
            if left > right:
                break
            
            for r in range(right, left - 1, -1):
                ans.append(matrix[bottom][r])
            bottom -= 1
            if top > bottom:
                break
                
            for b in range(bottom, top - 1, -1):
                ans.append(matrix[b][left])
            left += 1
            if left > right:
                break
                
        return ans


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(*mat, sep='\n')
    a = s.spiralOrder(mat)
    print()
    print(a)
