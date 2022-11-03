import java.util.Arrays;

public class L189 {
    
    public static void reverse(int[] nums, int i, int j){
        while (i < j){
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            i++;
            j--;
        }
    }

    public static void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n - k -1);
        reverse(nums, n-k, n-1);
        reverse(nums, 0, n-1);
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        rotate(nums, 10);
        System.out.println(Arrays.toString(nums));
    }
}
