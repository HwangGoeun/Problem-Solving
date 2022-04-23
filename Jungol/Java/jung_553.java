package Java;

import java.util.Scanner;

public class jung_553 {
    public static void main(String[] args) {
        int n, a = 0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                System.out.print(String.format("%c", 65 + a));
                a++;
            }
            System.out.println("");
        }

    }
    
}
