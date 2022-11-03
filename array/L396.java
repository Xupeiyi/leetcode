import java.util.Arrays;

public class L396 {

    public static int maxRotateFunction(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        
        // calculate F(0)
        int fval = 0;
        for (int i = 0; i < nums.length; i++){
            fval += nums[i] * i ;
        }

        int max = fval;
        for (int k = 0; k < nums.length-1; k++){
            // calcualte F(k+1) based on F(k)
            fval += sum - nums.length * nums[nums.length - 1 - k];

            // and update max
            max = Math.max(fval, max);
        }
        return max;
    }

    public static void main(String[] args){
        int[] nums = {4, 3, 2, 6};
        int ans = maxRotateFunction(nums);
        System.out.println(ans);
    }

}
