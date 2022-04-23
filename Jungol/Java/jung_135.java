package Java;

import java.util.Scanner;

public class jung_135 {
    public static void main(String[] args) {
        int a, b, num = 0;
        double sum = 0, avg;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        sc.close();

        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }

        for(int i = a; i <= b; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
                num++;
            }
        }
        avg = (int)sum / (double)num;
        System.out.println("sum : " + String.format("%.0f", sum));
        System.out.println("avg : " + String.format("%.1f", avg));

    }
    
}
