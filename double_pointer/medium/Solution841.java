public class Solution841 {
    public static String backspaceStr(String s){
        StringBuilder sb = new StringBuilder(s);
        int slow = 0;
        for (int fast = 0; fast < s.length(); fast++){
            if (s.charAt(fast) != '#') sb.setCharAt(slow++, s.charAt(fast));
            else slow = Math.max(slow-1, 0);
        }
        return sb.substring(0, slow);
    }
    
    public static boolean backspaceCompare(String s, String t) {
        return backspaceStr(s).equals(backspaceStr(t));
    }
}
