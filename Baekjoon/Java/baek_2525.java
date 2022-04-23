import java.util.Scanner;

public class baek_2525 {
    public static void main(String[] args) {
        int hour, min, cook;
        Scanner sc = new Scanner(System.in);
        hour = sc.nextInt();
        min = sc.nextInt();
        cook = sc.nextInt();
        sc.close();
        min = min + cook;

        while (min > 59) {
            hour++;
            min = min - 60;

            while (hour == 24)
                hour = 0;
        }

        System.out.println(hour + " " + min);
    }
    
}
