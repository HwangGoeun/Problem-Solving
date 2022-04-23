package Java;

import java.util.Scanner;

public class jung_554 {
    public static void main(String[] args) {
        int n, k = 1, kk = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                System.out.print(String.format("%d ", k));
                k++;
            }
            for (int j = 0; j <= i; j++) {
                System.out.print(String.format("%c ", 65 + kk));
                kk++;
            }
            System.out.println("");
        }
    }
    
}
