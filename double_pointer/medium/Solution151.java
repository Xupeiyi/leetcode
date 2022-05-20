public class Solution151 {
    public static int prevNonBlank(String s, int curr){
        while (curr >= 0){
            if (s.charAt(curr) != ' ') break;
            curr--;
        }
        return curr;
    }

    public static int prevBlank(String s, int curr){
        while (curr >= 0){
            if (s.charAt(curr) == ' ') break;
            curr--;
        }
        return curr;
    }

    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        int curr = s.length() - 1;
        while (curr >= 0){
            int end = prevNonBlank(s, curr);
            if (end < 0) break;
            curr = prevBlank(s, end);
            sb.append(' ');
            sb.append(s.substring(curr+1, end+1));
        }
        sb.deleteCharAt(0);
        return sb.toString();
    }
}
