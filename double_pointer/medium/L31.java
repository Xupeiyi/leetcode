import java.util.Arrays;

public class L31 {

    public static void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public static void nextPermutation(int[] nums) {
        // from end to start, find the number that breaks the increasing order
        // for example, for 2431, find number 2
        // 2 is number need to be updated first because 431 is already the largest "subnumber"
        int beforeStart = -1;
        for (int i = nums.length-1; i > 0; i--){
            if (nums[i-1] < nums[i]){
                beforeStart = i - 1;
                break;
            }
        }
        // if there's such a number i, swap it with number j
        // number j is the smallest number larger than i in nums[]
        if (beforeStart > -1) {
            for (int i = nums.length-1; i > beforeStart; i--){
                if (nums[i] > nums[beforeStart]) {
                    swap(nums, i, beforeStart);
                    break;
                }
            }
        }

        // reverse nums[beforeStart + 1:]
        int i = beforeStart + 1;
        int j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
}
