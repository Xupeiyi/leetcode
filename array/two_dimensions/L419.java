public class L419 {

    public static boolean isHead(char[][] board, int i, int j){
        if (board[i][j] == 'X'){
            if ((i-1 >= 0) && (board[i-1][j] == 'X')){
                return false;
            }
            if ((j-1 >= 0) && (board[i][j-1] == 'X')){
                return false;
            }
            return true;
        }
        return false;
    }

    public static int countBattleships(char[][] board) {
        int ans = 0;
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                if (isHead(board, i, j)){
                    ans += 1;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        char[][] board = {{'X', '.', '.', 'X'},
                          {'.', '.', '.', 'X'},
                          {'.', '.', '.', 'X'}};

        int ans = countBattleships(board);
        System.out.println(ans);
    }
}