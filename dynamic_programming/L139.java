import java.util.*;

public class L139{
    public static boolean wordBreak(String s, List<String> wordDict){
        ArrayList<Boolean> dp = new ArrayList<>(Collections.nCopies(s.length()+1, false)); 
        dp.set(0, true);
        for (int i = 0; i < s.length(); i++){
            for (int j = 0; j < wordDict.size(); j++){
                String word = wordDict.get(j);
                int start = i + 1 - word.length();
                if (start >= 0 && s.substring(start, i+1).equals(word) && dp.get(start)){
                    dp.set(i+1, true);
                    break;
                }
            }
        }
        return dp.get(dp.size()-1);
    }

    public static void main(String args[]){
        String s = "leetcode";
        ArrayList<String> wordDict = new ArrayList<>(List.of("le", "et", "etc", "code"));
        boolean ans = wordBreak(s, wordDict);
        System.out.println(ans);
    }
}