import java.util.Scanner;

public class SumTwoNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("กรอกจำนวนเต็ม 2 ค่า: ");
        int a = sc.nextInt();
        int b = sc.nextInt();

        int sum = a + b;
        System.out.println("ผลบวก = " + sum);
    }
}
