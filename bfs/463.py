def adjacents(grid, coord):
    nrow = len(grid)
    ncol = len(grid[0])
    row, col = coord
    ans = []
    for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        r = row + i
        c = col + j
        if 0 <= r < nrow and 0 <= c < ncol and grid[r][c]:
            ans.append((r, c))
    return ans


class Solution:
    def islandPerimeter(self, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        # find a starting point
        start = None
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1:
                    start = (row, col)
                    break
            else:
                continue
            break
        if not start:
            return 0
        
        perimeter = 0
        paths = [start]  # a stack
        visited = set()
        while paths:
            end = paths.pop()
            if end not in visited:
                visited.add(end)
                to_be_explored = adjacents(grid, end)
                perimeter += 4 - len(to_be_explored)
                
                for coord in to_be_explored:
                    if coord not in visited:
                        paths.append(coord)
        return perimeter


if __name__ == '__main__':
    s = Solution()
    # grid = [[0, 1, 0, 0],
    #         [1, 1, 1, 1],
    #         [0, 1, 0, 0],
    #         [1, 1, 0, 0]]
    # grid = [[0],
    #         [1]]
    grid = [[1, 1],
            [1, 1]]
    ans = s.islandPerimeter(grid)
    print(ans)