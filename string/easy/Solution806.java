public class Solution806 {
    public int[] numberOfLines(int[] widths, String s) {
        int[] ans = {0, 0};
        int sum = 0;
        for (int i = 0; i < s.length(); i++){
            int width = widths[s.charAt(i) - 'a'];
            if (sum + width > 100){
                ans[0] += 1;
                sum = width;
            }
            else{
                sum += width;
            }
        }
        ans[0] += 1;
        ans[1] = sum;
        return ans;
    }
}