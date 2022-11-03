public class L661 {

    public static int[][] calPrefix2D(int[][] arr){
        int nRows = arr.length;
        int nCols = arr[0].length;
        int[][] prefix2D = new int[nRows][nCols];
        
        // 1. fill in first row
        prefix2D[0][0] = arr[0][0];
        for (int i = 1; i < nCols; i++){
            prefix2D[0][i] = prefix2D[0][i-1] + arr[0][i];
        }
        for (int i = 1; i < nRows; i++){
            prefix2D[i][0] = prefix2D[i-1][0] + arr[i][0];
        }

        // f(i, j) = f(i-1, j) + f(i, j-1) - f(i-1, j-1) + arr[i][j]
        for (int i = 1; i < nRows; i++){
            for (int j = 1; j < nCols; j++){
                prefix2D[i][j] = prefix2D[i-1][j] + prefix2D[i][j-1] - prefix2D[i-1][j-1] + arr[i][j];
            }
        }
        return prefix2D;
    }

    public static int getPrefix(int[][] prefix2D, int i, int j){
        int nRows = prefix2D.length;
        int nCols = prefix2D[0].length;
        return ((i < 0) || (j < 0))?0:prefix2D[Math.min(i, nRows-1)][Math.min(j, nCols-1)];
    }

    public static int calSubMtxSum(int[][] prefix2D, int startRow, int startCol, int endRow, int endCol){
        return getPrefix(prefix2D, endRow, endCol) 
            - getPrefix(prefix2D, startRow-1, endCol) 
            - getPrefix(prefix2D, endRow, startCol-1) 
            + getPrefix(prefix2D, startRow-1, startCol-1);
    }

    public static int nAdjacents(int nRows, int nCols, int startRow, int startCol, int endRow, int endCol){
        startRow = Math.max(startRow, 0);
        startCol = Math.max(startCol, 0);
        endRow = Math.min(endRow, nRows-1);
        endCol = Math.min(endCol, nCols-1);
        return (endRow - startRow + 1) * (endCol - startCol + 1);
    }

    public static int[][] imageSmoother(int[][] img) {
        int nRows = img.length;
        int nCols = img[0].length;
        int[][] smoothImg = new int[nRows][nCols];
        int[][] prefix2D = calPrefix2D(img);
        for (int i = 0; i < nRows; i++){
            for(int j = 0; j < nCols; j++){
                smoothImg[i][j] = calSubMtxSum(prefix2D, i-1, j-1, i+1, j+1) / nAdjacents(nRows, nCols, i-1, j-1, i+1, j+1);
            }
        }
        return smoothImg;
    }

    public static void main(String[] args) {
        int[][] mtx = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] pfx = calPrefix2D(mtx);
        int ans = calSubMtxSum(pfx, 1, 1, 2, 2);
        System.out.println(ans);
    }
}
