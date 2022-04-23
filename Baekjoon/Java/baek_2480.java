import java.util.Scanner;

public class baek_2480 {
    public static int Max(int one, int two, int three) {
        int max = one;

        if (max < two)
            max = two;
        if (max < three)
            max = three;

        return max;
    }
    public static void main(String[] args) {
        int one, two, three, price, same;
        Scanner sc = new Scanner(System.in);
        one = sc.nextInt();
        two = sc.nextInt();
        three = sc.nextInt();
        sc.close();
        
        if (one == two && one == three)
            price = 10000 + one * 1000;
        else if (one == two || two == three || one == three) {
            same = one;
            if (same != two || same != three)
                same = two;
            price = 1000 + same * 100;
        }
        else {
            price = Max(one, two, three) * 100;
        }

        System.out.println(price);
    }
    
}
