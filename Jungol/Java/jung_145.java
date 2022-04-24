package Java;

import java.util.Scanner;

public class jung_145 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-i-1; j++) {
                System.out.print("  ");
            }
            for (int j = 0; j < i+1; j++) {
                System.out.print(String.format("%d ", j+1));
            }
            System.out.println("");
        }
    }
    
}
