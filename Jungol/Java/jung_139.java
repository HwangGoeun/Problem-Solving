package Java;

import java.util.Scanner;

public class jung_139 {
    public static void main(String[] args) {
        int a, b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        sc.close();

        if(a > b) {
            for(int i = 1; i < 10; i++) {
                for(int j = a; j >= b; j--) {
                    System.out.print(String.format("%d * %d =%3d   ", j, i, j * i));
                }
                System.out.println("");
            }
        }
        else {
            for(int i = 1; i < 10; i++) {
                for(int j = a; j <= b; j++) {
                    System.out.print(String.format("%d * %d =%3d   ", j, i, j * i));
                }
                System.out.println("");
            }
        }
    }
    
}
