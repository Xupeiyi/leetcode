public class Solution713 {
    public static int numSubarrayProductLessThanK(int[] nums, int k){
        if (k <= 1) return 0;
        int start = 0;
        int ans = 0;
        int prod = 1;
        // focus on what's new in the window
        // in this case, it's the nums[end] that brings new answers
        for (int end = 0; end < nums.length; end++){
            prod *= nums[end];
            while (prod >= k){
                prod /= nums[start];
                start++;
            }
            ans += end - start + 1;
        }
        return ans;
    }

    public static void main(String[] args){
        int[] nums = {10, 5, 2, 6};
        int ans = numSubarrayProductLessThanK(nums, 100);
        System.out.println(ans);
    }
}
