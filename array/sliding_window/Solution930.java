public class Solution930 {
    public static int numSubarraysWithSum(int[] nums, int goal) {
        int ans = 0;
        int start1 = 0;
        int start2 = 0;
        int sum1 = 0;
        int sum2 = 0;
        // use two sliding windows and calculate the length diff 
        for(int end = 0; end < nums.length; end++){
            sum1 += nums[end];
            sum2 += nums[end];
            while (start1 <= end && sum1 > goal) sum1 -= nums[start1++];
            while (start2 <= end && sum2 >= goal) sum2 -= nums[start2++];
            ans += start2 - start1;
        }
        return ans;
    }

    public static void main(String[] args){
        int[] nums = {0, 0, 0, 0, 0};
        int ans = numSubarraysWithSum(nums, 0);
        System.out.println(ans);
    }
}
