import java.util.HashMap;

class L219 {
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> positions = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (!positions.containsKey(nums[i])){
                positions.put(nums[i], i);
            }
            else{
                if (i - positions.get(nums[i]) <= k){
                    return true;
                }
                else{
                    positions.put(nums[i], i);
                }
            }
        }
        return false;
    }
}