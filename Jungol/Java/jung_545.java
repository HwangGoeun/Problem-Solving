package Java;

import java.util.Scanner;

public class jung_545 {
    public static void main(String[] args) {
        int number, three = 0, five = 0;
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i  < 10; i++) {
            number = sc.nextInt();
            if (number % 3 == 0)
                three++;
            if (number % 5 == 0)
                five++;
        }
        sc.close();

        System.out.println("Multiples of 3 : " + three);
        System.out.println("Multiples of 5 : " + five);

    }

}