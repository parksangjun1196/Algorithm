import java.util.*;
class Solution {
    public int[] solution(long n) {
        List<Integer> intarr = new ArrayList<>();
        int[] answer = {};
        String[] str = (n+"").split("");
        System.out.println(str.length);
        int len = str.length -1;
        int[] rstintarr = new int[len+1];
        int inx = 0;
        for (int i = 0; i < len+1; i++) {

            rstintarr[inx] = Integer.parseInt(str[len-i]);
            inx += 1;
            
        }
        return rstintarr;
    }
}