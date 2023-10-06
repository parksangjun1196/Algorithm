class Solution {
    boolean solution(String s) {
        boolean answer = true;
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

        s = s.toLowerCase();
        String[] strarr = new String[s.length()];
        String[] sarr = s.split("");
        int pscore = 0;
        int yscore = 0;
    
        for (int i = 0; i < s.length(); i++) {

            if (sarr[i].equals("y")) {
                yscore += 1;
            }
            else if (sarr[i].equals("p")) {
                pscore += 1;
            }
        }

        if (pscore != yscore) {
            answer = false;
        }
        return answer;
    }
}