public class Solution2024 {
    public static int maxConsecutiveChoice(String answerKey, Character choice, int k){
        // contains up to k non-choices in the window

        int start = 0;
        int maxLength = 0;
        for (int end = 0; end < answerKey.length(); end++){
            if (answerKey.charAt(end) != choice){
                if (k > 0){
                    k--;
                }
                // update the lower boundary of the window
                else{
                    // update maxLength
                    maxLength = Math.max(end - start, maxLength);

                    // exclude a non-choice (and all previous choices) from the window
                    while (start <= end && answerKey.charAt(start) == choice){
                        start++;
                    }
                    start++;
                }
            }
        }
        return Math.max(answerKey.length() - start, maxLength);
    }

    public static int maxConsecutiveAnswers(String answerKey, int k) {
        int ansT = maxConsecutiveChoice(answerKey, 'T', k);
        int ansF = maxConsecutiveChoice(answerKey, 'F', k);
        return Math.max(ansT, ansF);
    }

    public static void main(String[] args) {
        int ans = maxConsecutiveAnswers("TTFTT", 1);
        System.out.println(ans);
    }
}
    
