import java.util.*;
import java.io.*;
import java.lang.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        long test = (long)Math.sqrt(n);
        if (test*test == n){
            answer = (test+1)*(test+1);
        }
        else {
            answer = -1;
        }
        return answer;
    }
}