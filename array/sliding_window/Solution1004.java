public class Solution1004 {
    public static int longestOnes(int[] nums, int k) {
        if (nums.length <= k){
            return k;
        } 

        int start = 0;
        int sum = 0;

        for (int end = 0; end < nums.length; end++){
            sum += nums[end];
            if (sum + k < end - start + 1){
                sum -= nums[start++];
            }
        }
        return nums.length - start;
    }

    public static void main(String[] args){
        int[] nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
        int ans = longestOnes(nums, 3);
        System.out.println(ans);
    }
}
