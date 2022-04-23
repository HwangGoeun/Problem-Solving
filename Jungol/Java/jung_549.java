package Java;

import java.util.Scanner;

public class jung_549 {
    public static void main(String[] args) {

        int n, sum = 0, add, cnt = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
    
        for(add = 1; sum < n; add += 2) {
            sum += add;
            cnt++;
        }
    
        System.out.println(String.format("%d %d", cnt, sum));
        
    }
}
