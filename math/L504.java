import java.lang.Math;

public class L504{

    public static String convertToBase7(int num){
        if (num == 0) {
            return "0";
        }
        boolean negative = (num < 0);
        num = Math.abs(num);
        StringBuffer digits = new StringBuffer();
        while (num > 0) {
            digits.append(num % 7);
            num /= 7;
        }
        if (negative) {
            digits.append('-');
        }
        return digits.reverse().toString();
    }

    public static void main(String[] args){
        String ans = convertToBase7(-100);
        System.out.println(ans);
    }

}