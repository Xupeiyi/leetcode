public class Solution209 {
    public static int minSubArrayLen(int target, int[] nums) {
        int start = 0;
        int sum = 0;
        Integer minLen = Integer.MAX_VALUE;
        for (int end = 0; end < nums.length; end++){
            sum += nums[end];

            // update lower boundary of window
            // if sum of subArray after removing the first element 
            // is still greater than or equal to target, remove the first element  
            while(start < end && sum - nums[start] >= target) {
                sum -= nums[start];  // update status first
                start += 1;          // then renew lower boundary
            }

            // when to update the result
            if (sum >= target){
                minLen = Math.min(end - start + 1, minLen);
            }
        }
        return (minLen < Integer.MAX_VALUE)? minLen:0;
    }
    public static void main(String[] args){
        int[] nums = {2, 3, 1, 2, 4, 3};
        minSubArrayLen(7, nums);
    }
}
