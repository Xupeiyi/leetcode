public class Solution567 {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()){
            return false;
        }
         
        
        // record differences
        int[] count = new int[26];
        for (int i = 0; i < s1.length(); i++){
            count[s2.charAt(i) - 'a']++;
            count[s1.charAt(i) - 'a']--;
        }

        // count differences
        int diff = 0;
        for (int i = 0; i < count.length; i++){
            if (count[i] != 0){
                diff++;
            }
        }
        if (diff == 0){
            return true;
        }

        for (int i = 0; i < s2.length() - s1.length(); i++){
            // s[i] count changes            
            int startIdx = s2.charAt(i) - 'a';
            if (count[startIdx] == 1) diff--;
            else if (count[startIdx] == 0) diff++;
            count[startIdx]--;
            
            // s[i + p.lenth()] changes
            int endIdx = s2.charAt(i + s1.length()) - 'a';
            if (count[endIdx] == -1) diff--;
            else if (count[endIdx] == 0) diff++;
            count[endIdx]++;

            if (diff == 0){
                return true;
            }
        }
        return false;
    }
}
