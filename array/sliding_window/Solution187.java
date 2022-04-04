import java.util.*;

public class Solution187 {
    static final int L = 10;
    HashMap<Character, Integer> bin = new HashMap<Character, Integer>() {{
        put('A', 0);
        put('C', 1);
        put('G', 2);
        put('T', 3);
    }};

    public List<String> findRepeatedDnaSequences(String s){
        List<String> ans = new ArrayList<>();
        int n = s.length();
        if (n <= L){
            return ans;
        }

        // initialize string in the window (it has 9 characters)
        int x = 0;
        for (int i = 0 ; i < L-1; i++){
            x = (x << 2) | bin.get(s.charAt(i));
        }

        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i <= n - L; i++){
            //  include new digits;                        take the lowest 20 digits
            x = ((x << 2) | bin.get(s.charAt(i + L - 1))) & ((1 << (L*2)) - 1);
            count.put(x, count.getOrDefault(x, 0) + 1);
            if (count.get(x) == 2){
                ans.add(s.substring(i, i + L));
            }
        }
        return ans;
    }

}
