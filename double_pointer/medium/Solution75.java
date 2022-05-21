class Solution {
    public void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public void sortColors(int[] nums) {
        int redIdx = 0;
        int blueIdx = nums.length - 1;
        for (int i = 0; i <= blueIdx; i++){
            if (nums[i] == 0) swap(nums, i, redIdx++);
            // 注意i--。要保证三个不变量： nums[:redIdx] == 0
            //                           nums[blueIdx+1:] == 2
            //                           nums[redIdx:i] == 1
             // 不要忽略最后一个 
            else if (nums[i] == 2) swap(nums, i--, blueIdx--); 

        }
    }
}