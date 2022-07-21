package Java;

import java.util.Scanner;

public class jung_149 {
    public static void main(String[] args) {
        int n, a = 1;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(String.format("%d ", a));
                a += 2;
                if (a > 9)
                    a = 1;
            }
            System.out.println("");
        }
    }
    
}
