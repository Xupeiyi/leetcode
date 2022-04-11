import java.util.ArrayList;
import java.util.List;

public class Solution438 {
    public static List<Integer> findAnagrams(String s, String p){
        List<Integer> ans = new ArrayList<>();
        if (s.length() < p.length()){
            return ans;
        }
        
        // record differences
        int[] count = new int[26];
        for (int i = 0; i < p.length(); i++){
            count[s.charAt(i) - 'a']++;
            count[p.charAt(i) - 'a']--;
        }

        // count differences
        int diff = 0;
        for (int i = 0; i < count.length; i++){
            if (count[i] != 0){
                diff++;
            }
        }
        if (diff == 0){
            ans.add(0);
        }

        for (int i = 0; i < s.length() - p.length(); i++){
            // s[i] count changes            
            int startIdx = s.charAt(i) - 'a';
            if (count[startIdx] == 1) diff--;
            else if (count[startIdx] == 0) diff++;
            count[startIdx]--;
            
            // s[i + p.lenth()] changes
            int endIdx = s.charAt(i + p.length()) - 'a';
            if (count[endIdx] == -1) diff--;
            else if (count[endIdx] == 0) diff++;
            count[endIdx]++;

            if (diff == 0){
                ans.add(i + 1);
            }
        }
        return ans;
    }
}
