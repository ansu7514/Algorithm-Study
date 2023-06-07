
import java.util.Arrays;

class Solution {
public String solution(String s) {

String answer = "";
String [] arr = s.split(" ");
int[] result = Arrays.stream(arr).mapToInt(Integer::parseInt).toArray();
Arrays.sort(result);
answer = result[0]+" "+result[arr.length-1];
return answer;
}
}