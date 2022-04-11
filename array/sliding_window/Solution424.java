public class Solution424 {
    public int characterReplacement(String s, int k) {
        if (s == null){
            return 0;
        }
        int[] count = new int[26];
        int start = 0;     // 因为找到最大值即可，窗口并不需要收窄。并不需要维护一个在窗口内恒成立的条件。
        int maxCount = 0;  // maxCount并不需要是“窗口内”字母的最大出现次数 
        for (int end = 0; end < s.length(); end++){
            int key = s.charAt(end) - 'A';
            count[key]++;
            maxCount = Math.max(maxCount, count[key]);
            if (end - start + 1 > maxCount + k){
                count[s.charAt(start) - 'A']--;
                start++;
            }
        }
        return s.length() - start;
    }
}
