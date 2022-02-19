def nearby(coord, nrows, ncols):
    x, y = coord
    
    return [(i, j) for (i, j) in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            if 0 <= i <= nrows-1 and 0 <= j <= ncols-1]
    

class Solution:
    def exist(self, board, word: str) -> bool:
        ans = False
        nrows = len(board)
        ncols = len(board[0])
        
        used = [[0 for _ in range(ncols)] for _ in range(nrows)]
        
        def backtrack(start, idx):
            nonlocal ans, used
            
            if idx == len(word):
                ans = True
                return
            
            for i, j in nearby(start, nrows, ncols):
                if used[i][j] == 0 and board[i][j] == word[idx]:
                    used[i][j] = 1
                    backtrack((i, j), idx+1)
                    used[i][j] = 0
        
        for i in range(nrows):
            for j in range(ncols):
                if ans:
                    break
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    backtrack((i, j), 1)
                    used[i][j] = 0
                    
        return ans
    
        
if __name__ == '__main__':
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    ans = s.exist(board, "ABCCED")
    print(ans)
    
    ans = s.exist(board, "DECC")
    print(ans)
    
    ans = s.exist(board, "ABCB")
    print(ans)
    
    ans = s.exist(board, "SEE")
    print(ans)