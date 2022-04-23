package Java;

import java.util.Scanner;

public class jung_552 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();
        int k = n;

        for(int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < (k * 2 - 1); j++) {
                System.out.print("*");
            }
            k--;
            System.out.println("");
        }
        
    }
}
