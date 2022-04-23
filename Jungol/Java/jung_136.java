package Java;

import java.util.Scanner;

public class jung_136 {
    public static void main(String[] args) {
        int num;
        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();
        sc.close();

        for(int i = 1; i <= 10; i++) {
            System.out.print((num * i) + " ");
        }
    }
    
}
