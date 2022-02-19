########################################
##### Solution 1
#########################################
# def count(board):
#     x, o = 0, 0
#     for row in board:
#         for pos in row:
#             if pos == 'X':
#                x += 1
#             if pos == 'O':
#                 o += 1
#     return x, o
#
#
# def straight3(row, piece):
#     return row[0] == piece and row[1] == piece and row[2] == piece
#
#
# def win(board, piece):
#     rows = [[pos for pos in row] for row in board]
#     columns = [[board[r][c]for r in range(3)] for c in range(3)]
#     cross = [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
#     return any(map(lambda x: straight3(x, piece), rows + columns + cross))
#
#
# class Solution:
#     def validTicTacToe(self, board):
#         x, o = count(board)
#
#         if win(board, 'X'):
#             return not win(board, 'O') and o == x-1
#         elif win(board, 'O'):
#             return not win(board, 'X') and x == o
#         return x-o == 1 or x-o == 0
###################################
#### Solution 2
###################################


def discard_chances(chances, row, col):
    chances[0].discard(row)
    chances[1].discard(col)
    chances[2].discard(row-col)
    chances[2].discard(row+col)


class Solution:
    def validTicTacToe(self, board):
        x, o = 0, 0
        xchances = [{0, 1, 2}, {0, 1, 2}, {0, 2}]
        ochances = [{0, 1, 2}, {0, 1, 2}, {0, 2}]
        
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    x += 1
                    discard_chances(xchances, row, col)
                elif board[row][col] == 'O':
                    o += 1
                    discard_chances(xchances, row, col)
                else:
                    discard_chances(ochances, row, col)
                    discard_chances(xchances, row, col)
                    
        win_x = any(xchances)
        win_o = any(ochances)
        if win_x:
            return not win_o and o == x-1
        elif win_o:
            return not win_x and x == o
        return x-o == 1 or x-o == 0
        

if __name__ == '__main__':
    board = ["XOX", "O O", "XOX"]
    s = Solution()
    print(s.validTicTacToe(board))
