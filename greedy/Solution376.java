class Solution376 {
    public static int nextFarthestNumber(int[] nums, int start, boolean greatest){
        // find the nearest index of a number that has the furthest distance to nums[start]
        // move one step forward only when the next number is valid
        int end = start;
        if (greatest){
            while (end < nums.length-1 && nums[end] <= nums[end+1]) end++;
        }
        else{
            while (end < nums.length-1 && nums[end] >= nums[end+1]) end++;
        }
        return end;
    } 

    public static int wiggleMaxLength(int[] nums) {
        // The diff array may not be used. But the edge cases must be thought over thoroughly.
        int ans = 1;

        // skip the identical numbers
        int curr = 0;
        while(curr < nums.length-1 && nums[curr+1] == nums[curr]) curr++;

        // find the next largest/smallest number
        boolean greatest = (nums[curr+1] > nums[curr])? true: false;
        while (curr < nums.length - 1){
            int nextCurr = nextFarthestNumber(nums, curr, greatest);
            if (nextCurr < nums.length && nums[nextCurr] != nums[curr]) ans++;
            greatest = !greatest;
            curr = nextCurr;
        }
        return ans;
    }

    public static void main(String[] args){
        int[] nums = {1, 1, 1, 17, 5, 10, 13, 15, 10, 5, 16, 8, 8, 8};
        int ans = wiggleMaxLength(nums);
        System.out.println(ans);
    }
}