from typing import List
from ufset import UnionFindSet


def boarder(nrows, ncols):
    if nrows == 1:
        return [(0, c) for c in range(ncols)]
    
    if ncols == 1:
        return [(r, 0) for r in range(ncols)]
    
    return [(0, c) for c in range(ncols-1)] \
         + [(r, ncols-1) for r in range(nrows-1)] \
         + [(nrows-1, c) for c in range(1, ncols)] \
         + [(r, 0) for r in range(1, nrows)]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows = len(board)
        ncols = len(board[0])
        
        def idx(x, y):
            return x * ncols + y
        
        def is_O(x, y):
            return board[x][y] == 'O'
        
        def adjacent_Os(x, y):
            return [
                (i, j) for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                if 0 <= i and i < nrows and 0 <= j and j < ncols and is_O(i, j)
            ]
            

        dummy = nrows * ncols
        uf = UnionFindSet(nrows*ncols + 1)

        for x, y in boarder(nrows, ncols):
            if is_O(x, y):
                uf.union(idx(x, y), dummy)
        
        for x in range(1, nrows-1):
            for y in range(1, ncols-1):
                if is_O(x, y):
                    for i, j in adjacent_Os(x, y):
                        uf.union(idx(x, y), idx(i, j))
        
        for x in range(1, nrows-1):
            for y in range(1, ncols-1):
                if not uf.is_connected(idx(x, y), dummy):
                    board[x][y] = 'X'


if __name__ == '__main__':
    s = Solution()
    bd_coords = boarder(3, 3)
    print(bd_coords)

    board = [["X","O","X"],["X","O","X"],["X","O","X"]]
    s.solve(board)
    print(*board, sep='\n')