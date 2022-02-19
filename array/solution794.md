### 解题思路
本题的基本思路并不难。先数出棋盘中'X', 'O'的数量，然后分类判断即可：
- 如果玩家1赢了，则玩家2没有赢， 且'O'数量比'X'少1；
- 如果玩家2赢了，则玩家1没有赢，且'O'数量与'X'数量相同；
- 如果两人都没有赢，则'X'与'O'数量相同或比'O'多1.

思路用python3表示为：
``` python3
class Solution:
    def validTicTacToe(self, board):
        x, o = count(board)
        if win(board, 'X'):
            return not win(board, 'O') and o == x-1
        elif win(board, 'O'):
            return not win(board, 'X') and x == o
        return x-o == 1 or x-o == 0
```

如何判断玩家1或2获胜呢？许多答案的解法是这样的：
```python3
def win(board, piece):
    return (board[0][0] == piece and board[0][1] == piece and board[0][2] == piece) \
        or (board[1][0] == piece and board[1][1] == piece and board[1][2] == piece) \
        or ...
```
一共只有八种情况可以获胜，暴力枚举即可。
但是，在遍历棋盘数棋子的时候，就可以注意到某些获胜的条件已经不可能实现了。比如，如果在第一行第一列发现了'O'或' '，'X'就已经不可能通过在第一行连成三子，在第一列连成三子，或在左对角线连成三子获胜了。随着遍历的进行，玩家1和玩家2获胜的方式逐渐减少。在遍历结束时，就已经可以确定谁通过哪种方式获胜。

其实对于本题来说由于情况很少暴力枚举就已经足够，甚至更快一些，但我还是想试试这种思路。代码实现如下：

### 代码

```python3
def discard_chances(chances, row, col):
    chances[0].discard(row)
    chances[1].discard(col)
    chances[2].discard(row-col)
    chances[2].discard(row+col)


class Solution:
    def validTicTacToe(self, board):
        x, o = 0, 0  # 棋盘中'X', 'O'的数量
        # xchances中的三个集合分别代表通过连成行，列，对角线获胜的机会
        # 前两个集合中的0，1，2代表能够在哪一行/列连成三子获胜
        # 第三个集合的用法较特殊。如果棋子在i行j列，如果i == j
        # 即i-j==0则可以通过连成左对角线获胜。如果 i == 2 - j
        # 即 i + j == 2 则可以通过连成右对角线获胜。
        xchances = [{0, 1, 2}, {0, 1, 2}, {0, 2}]  
        ochances = [{0, 1, 2}, {0, 1, 2}, {0, 2}]
        
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    x += 1
                    # 'O'失去了利用当前位置获胜的机会
                    discard_chances(ochances, row, col)
                elif board[row][col] == 'O':
                    o += 1
                    # 'X'失去了利用当前位置获胜的机会
                    discard_chances(xchances, row, col)
                else:
                    # 'X','O'都失去了利用当前位置获胜的机会
                    discard_chances(ochances, row, col)
                    discard_chances(xchances, row, col)
                    
        win_x = any(xchances)
        win_o = any(ochances)
        if win_x:
            return not win_o and o == x-1
        elif win_o:
            return not win_x and x == o
        return x-o == 1 or x-o == 0
```