package Java;

import java.util.Scanner;

public class jung_137 {
    public static void main(String[] args) {
        int r, c;
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt();
        c = sc.nextInt();
        sc.close();

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(((i + 1) * (j + 1)) + " ");
            }
            System.out.println("");
        }
    }
    
}
