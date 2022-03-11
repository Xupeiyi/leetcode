from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        max_length = 0
        dp = []        
        for i in range(nrows):
            row = []
            for j in range(ncols):
                num = int(matrix[i][j])
                if num:
                    max_length = 1
                row.append(num)
            dp.append(row)

        
        for i in range(1, nrows):
            for j in range(1, ncols):
                if dp[i][j] and dp[i][j-1] and dp[i-1][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_length = max(max_length, dp[i][j])

        return max_length * max_length


if __name__ == '__main__':
    s = Solution()
    mat = [["1","0","1","1","1"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"],
           ["1","0","0","1","0"]]

    mat = [["0","0","0","1"],
           ["1","1","0","1"],
           ["1","1","1","1"],
           ["0","1","1","1"],
           ["0","1","1","1"]]

    mat = [["0","0","0","0","0"],
            ["0","0","0","0","0"],
            ["0","0","0","0","1"],
            ["0","0","0","0","0"]]
    ans = s.maximalSquare(mat)
    print(ans)