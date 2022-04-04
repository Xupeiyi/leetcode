import java.util.TreeSet;


/*The elements in the window can be rearranged, sorted, or changed*/
public class Solution220 {
    public static boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> sortedSubArrayK = new TreeSet<>();
        for (int i = 0; i < nums.length; i++){
            if (sortedSubArrayK.size() == k+1){
                sortedSubArrayK.remove((long)nums[i-k-1]);
            }
            // search for a y in the treeset, that nums[i] - t <= y <= nums[i] + t
            // which is, y >= nums[i] - t , y <= nums[i] + t 

            Long y = sortedSubArrayK.ceiling((long)nums[i] - t);
            if (y != null && y <= (long)nums[i] + t){
                return true;
            }

            sortedSubArrayK.add((long)nums[i]);
        }
        return false;
    }

    public static void main(String[] args){
        int[] nums = {1, 5, 9, 1, 5, 9};
        boolean ans = containsNearbyAlmostDuplicate(nums, 2, 3); 
        System.out.println(ans);
    }
}
