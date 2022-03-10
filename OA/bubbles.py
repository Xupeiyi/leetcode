def solutions(bubbles):
    nrows = len(bubbles)
    ncols = len(bubbles[0])
    
    def check_same_color(i, j):
        adjacents = [(ni, nj) for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] 
                     if 0 <= ni < nrows and 0 <= nj < ncols]
        same_color = [(ni, nj) for ni, nj in adjacents if bubbles[ni][nj] == bubbles[i][j]]
        return same_color + [(i, j)] if len(same_color) >= 2 else []
    
    same_color_coords = set()

    for i in range(nrows):
        for j in range(ncols):
            same_color_coords |=  set(check_same_color(i, j))
    
    for i, j in same_color_coords:
        bubbles[i][j] = 0

    for j in range(ncols):
        slow = nrows - 1
        for i in range(nrows-1, -1, -1):
            if bubbles[i][j] != 0:
                bubbles[slow][j] = bubbles[i][j]
                slow -= 1
        for i in range(slow, -1, -1):
            bubbles[i][j] = 0
    return bubbles


if __name__ == '__main__':
    bubbles = [[3, 1, 2, 1], 
               [1, 1, 1, 4], 
               [3, 1, 2, 2],
               [3, 3, 3, 4]]

    ans = solutions(bubbles)
    print(ans)