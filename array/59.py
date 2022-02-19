###################################################
# 解法1
# 一直前进，直到碰到边界，然后转向。如果转向后仍碰到边界说明已经无路可走。
###################################################


def direction_generator():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i = -1
    while True:
        i = (i + 1) % 4
        yield directions[i]
        

def at_boundary(matrix, n, coord, direction):
    next_coord = move(coord, direction)
    i, j = next_coord[0], next_coord[1]
    return i >= n or j >= n or matrix[i][j] != 0
    

def fill_matrix(matrix, coord, num):
    i, j = coord[0], coord[1]
    matrix[i][j] = num


def move(coord, direction):
    return coord[0] + direction[0], coord[1] + direction[1]


class Solution1:
    def generateMatrix(self, n: int):
        turn_right = direction_generator()
        mat = [[0] * n for i in range(n)]
        coord = (0, -1)
        num = 0
        direction = next(turn_right)
        while True:
            
            # 沿当前方向填充矩阵, 直到到达边界
            while not at_boundary(mat, n, coord, direction):
                num += 1
                coord = move(coord, direction)
                fill_matrix(mat, coord, num)
                
            # 到达边界后更换方向
            direction = next(turn_right)

            # 如果再次遇到障碍就停下
            if at_boundary(mat, n, coord, direction):
                return mat

###################################################
# 解法2
# 不需要每一步都判断是否碰到边界。该走多少步在一开始就能确定下来。
###################################################
from itertools import chain


def fill_clockwise(mat, n, coord, num):
    if n <= 0:
        return
    
    if n == 1:
        fill_matrix(mat, coord, num)
    
    # 顺时针填充外环
    i, j = coord[0], coord[1]
    length = n - 1
    fill_coords = chain(((i, j + k) for k in range(length)),
                        ((i + k, j + length) for k in range(length)),
                        ((i + length, j + length - k) for k in range(length)),
                        ((i + length - k, j) for k in range(length)),
                        )
    for fc in fill_coords:
        fill_matrix(mat, fc, num)
        num += 1
    
    fill_clockwise(mat, n-2, (i+1, j+1), num)


class Solution:
    
    def generateMatrix(self, n):
        mat = [[0] * n for i in range(n)]
        fill_clockwise(mat, n, (0, 0), 1)
        return mat
        

if __name__ == '__main__':
    s = Solution()
    ans = s.generateMatrix(4)
    for row in ans:
        print(row)