public class Solution11 {
    public static int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int max = Math.min(height[start], height[end]) * (end - start);
        while (start < end){
            if (height[start] <= height[end]){
                start++;
            }
            else{
                end--;
            }
            int area = Math.min(height[start], height[end]) * (end - start);
            max = Math.max(area, max);
        }
        return max;
    }  

    public static void main(String[] args) {
        int[] nums = {1,8,6,2,5,4,8,3,7};
        int ans = maxArea(nums);
        System.out.println(ans);
    }
}
