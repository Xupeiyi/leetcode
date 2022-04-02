import java.util.HashSet;

public class Solution3{
    public static int lengthOfLongestSubstring(String s){
        if (s.length() <= 1){
            return s.length();
        }

        int maxLength = 1;
        int start = 0;
        HashSet<Character> subStringLetters = new HashSet<>();
        subStringLetters.add(s.charAt(start));

        for (int i = 1; i < s.length(); i++){
            Character ch = s.charAt(i);
            
            if (subStringLetters.contains(ch)){
                maxLength = Math.max(i - start, maxLength);
                
                // update lower bound of the window
                // pop all characters in subStringLetters until ch is met
                while(s.charAt(start)!= ch){
                    subStringLetters.remove(s.charAt(start));
                    start++;
                }
                start++;
            }
            else{
                subStringLetters.add(ch);
            }
        }

        return Math.max(s.length() - start, maxLength);
    }

    public static void main(String[] args){
        int ans = lengthOfLongestSubstring("abcdbc");
        System.out.println(ans);
    }
}