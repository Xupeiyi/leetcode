from typing import List

def check_prev_status(x):
    return x & 0b01

def update_curr_status(x, nx):
    return nx << 1 | x

def get_curr_status(x):
    return x >> 1

def count_surrounding(board, i ,j):
    nrows, ncols = len(board), len(board[0])
    surroundings = [
        (ni, nj) for ni, nj in 
        [(i-1, j-1), (i-1, j), (i-1, j+1), 
         (i, j-1), (i, j+1),
         (i+1, j-1),(i+1, j), (i+1, j+1)
        ]
        if 0 <= ni < nrows and 0 <= nj < ncols
    ]

    return sum([check_prev_status(board[i][j]) for i, j in surroundings])


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows, ncols = len(board), len(board[0])
        for i in range(nrows):
            for j in range(ncols):
                cnt = count_surrounding(board, i, j)
                curr = board[i][j]
                if cnt == 2:
                    board[i][j] = update_curr_status(curr, curr)
                elif cnt == 3:
                    board[i][j] = update_curr_status(curr, 1)
                else:
                    board[i][j] = update_curr_status(curr, 0)
        
        for i in range(nrows):
            for j in range(ncols):
                board[i][j] = get_curr_status(board[i][j])
        
        return board