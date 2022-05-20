import java.util.*;

class Solution15 {

    public static int nextDiffNumIdx(int[] nums, int startIdx, int direction){
        int currIdx = startIdx + direction;
        while (currIdx >= 0  && currIdx < nums.length){
            if (nums[currIdx] != nums[startIdx]){
                break;
            }
            currIdx += direction;
        }
        return currIdx;
    }

    public static List<List<Integer>> findRestTwo(int[] nums, int curr){
        int start = curr + 1;
        int end = nums.length - 1;
        List<List<Integer>> answers = new ArrayList<>();
        while (start < end){
            if (nums[start] + nums[end] == -nums[curr]){
                List<Integer> answer = new ArrayList<>(List.of(nums[curr], nums[start], nums[end]));
                answers.add(answer);
                start = nextDiffNumIdx(nums, start, 1);
                end = nextDiffNumIdx(nums, end, -1);
            }
            else if (nums[start] + nums[end] < -nums[curr]) start = nextDiffNumIdx(nums, start, 1);
            else end = nextDiffNumIdx(nums, end, -1);
        }
        return answers;
    }


    public static List<List<Integer>> threeSum(int[] nums) {
        // 1. sort nums
        Arrays.sort(nums);

        // 2. loop over each element, skip the duplicated numbers
        List<List<Integer>> answers = new ArrayList<>();
        int i = 0;
        while (i < nums.length){
            
            // 3. find the rest two numbers
            answers.addAll(findRestTwo(nums, i));
            i = nextDiffNumIdx(nums, i, 1);
        }
        return answers;
    }

    public static void main(String[] args) {
        int[] arr1 = {-6, 1, 1, 2, 3, 3, 3, 4, 4};
        int idx1 = nextDiffNumIdx(arr1, 4, 1);
        System.out.println(arr1[idx1]);
        int idx2 = nextDiffNumIdx(arr1, 8, -1);
        System.out.println(arr1[idx2]);
        List<List<Integer>> ans = findRestTwo(arr1, 0);
        System.out.println(ans);
        
        int[] nums = {-1,0,1,2,-1,-4};
        List<List<Integer>> ans1 = threeSum(nums);
        System.out.println(ans1);
    }
}   