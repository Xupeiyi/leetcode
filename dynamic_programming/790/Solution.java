import java.util.*;


class Solution {
    public static int numTilings(int n) {
        if (n == 1){
            return 1;
        }
        HashMap<Integer, int[]> convertFrom = new HashMap<>();
        convertFrom.put(0, new int[]{3});
        convertFrom.put(1, new int[]{0, 2});
        convertFrom.put(2, new int[]{0, 1});
        convertFrom.put(3, new int[]{0, 1, 2, 3});
        
        long[][] dp = new long[n+1][4];
        dp[2][0] = 1;
        dp[2][1] = 1;
        dp[2][2] = 1;
        dp[2][3] = 2;

        for (int i = 3; i < n+1; i++){
            for (int j = 0; j < 4; j++){
                dp[i][j] = 0;
                for (int k: convertFrom.get(j)){
                    dp[i][j] += dp[i-1][k] ;   
                }
                dp[i][j] = dp[i][j] % (long)(Math.pow(10,9) + 7);
            }
        }
        
        return (int)dp[dp.length-1][3];    
    }

    public static void main(String[] args){
        int ans = numTilings(3);
        System.out.println(ans);
        return;
    }

}