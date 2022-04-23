package Java;

import java.util.Scanner;

public class jung_546 {
    public static void main(String[] args) {
        int sub, score;
        double sum = 0, avg;
        Scanner sc = new Scanner(System.in);

        sub = sc.nextInt();
        for(int i = 0; i < sub; i++) {
            score = sc.nextInt();
            sum += score;
        }
        sc.close();

        avg = sum / sub;
        System.out.println("avg : " + String.format("%.1f", avg));
        if (avg >= 80) 
            System.out.println("pass");
        else
            System.out.println("fail");

    }
    
}
