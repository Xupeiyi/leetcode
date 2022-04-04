import java.util.HashSet;

public class Solution904 {
    public static int totalFruit(int[] fruits) {
        HashSet<Integer> basket = new HashSet<>();
        int start = 0;
        int maxCount = 0;
        for (int end = 0; end < fruits.length; end++){
            if (!basket.contains(fruits[end])){
                
                // if basket is full, record current size, then update basket
                if (basket.size() == 2){
                    maxCount = Math.max(end - start, maxCount);

                    // update basket
                    basket.clear();
                    basket.add(fruits[end]);
                    basket.add(fruits[end-1]);
                    
                    // update start of the window
                    start = end;
                    while (start >= 0 && basket.contains(fruits[start-1])){
                        start -= 1;
                    }
                }
                else{
                    basket.add(fruits[end]);
                }
            }
        }
        return Math.max(fruits.length - start ,maxCount);
    }
}