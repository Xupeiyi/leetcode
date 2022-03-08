from typing import List
from collections import deque

def next_coords(i, j, nrows, ncols):
    potential_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(ni, nj) for ni, nj in potential_coords 
                if 0 <= ni < nrows and 0 <= nj < ncols]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        nrows = len(grid)
        ncols = len(grid[0])

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] == '0'
                    # bfs
                    # 使用bfs时有一个坑。发现陆地后要第一时间把该坐标置0，否则该坐标会被重复加入队列很多次
                    # 比如对grid = [[1, 1, 1, 1], 
                    #               [1, 1, 1, 1],
                    #               [1, 1, 1, 1]]
                    # 探索(0, 1)和(1, 0)时都会把(1, 1)加入队列
                    # 而使用dfs就不用第一时间置0

                    path = deque([(i, j)])
                    while path:
                        ci, cj = path.popleft()
                        # grid[ci][cj] = '0'
                        for ni, nj in next_coords(ci, cj, nrows, ncols):
                            if grid[ni][nj] == '1':
                                grid[ni][nj] = '0'
                                path.append((ni, nj))
        return count            

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]

    ans = s.numIslands(grid)
    print(ans)


