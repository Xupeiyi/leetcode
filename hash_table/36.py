from typing import List


def which_grid(i, j):
    return (i // 3) * 3 + (j // 3)


class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [set() for i in range(9)]  # todo: bit operation
        cols = [set() for i in range(9)]
        grids = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (not board[i][j] in rows[i]) and \
                        (not board[i][j] in cols[j]) and \
                        (not board[i][j] in grids[which_grid(i, j)]):
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grids[which_grid(i, j)].add(board[i][j])
                else:
                    return False
        return True


# 用位运算也可以实现哈希表
class Solution:

    def isValidSudoku(self,board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        box = [0]*9
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':continue
                num = 1<<int(board[i][j])
                b = (i//3)*3 + j//3
                if row[i]&num != 0 or col[j]&num != 0 or box[b]&num !=0 : return False
                row[i] |= num
                col[j] |= num
                box[b] |= num
        return True

if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    
    s = Solution()
    ans = s.isValidSudoku(board)
    print(ans)
