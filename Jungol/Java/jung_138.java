package Java;

import java.util.Scanner;

public class jung_138 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for(int i = 1; i <= n; i ++) {
            for(int j = 1; j <= n; j ++) {
                System.out.print(String.format("(%d, %d) ", i, j));
            }
            System.out.println("");
        }
    }
    
}
