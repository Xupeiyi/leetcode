import java.util.*;

public class interview0806{

    // 所谓“相信递归的力量”。并不需要知道具体是怎样实现的，假装已经实现了就行了。
    public static void hanota(List<Integer> A, List<Integer> B, List<Integer> C) {
        if (A.isEmpty()){
            return;
        }
        int nMoved = A.size() - 1; 
        hanota(A.subList(1, A.size()), C, B);
        int a = A.remove(0);
        C.add(a);
        hanota(B.subList(B.size()-nMoved, B.size()), A, C);
    }

    public static void main(String[] args){
        List<Integer> A = new ArrayList<>(List.of(3, 2, 1));
        List<Integer> B = new ArrayList<>(List.of());
        List<Integer> C = new ArrayList<>(List.of());
        hanota(A, B, C);
        System.out.println(C);
    }

}