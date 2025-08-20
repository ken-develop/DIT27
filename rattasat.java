import java.util.Scanner;

public class AddTwoNumbers {

    // เมธอดหลัก
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // รับข้อมูลจำนวนเต็มตัวที่ 1
            System.out.print("กรุณาใส่จำนวนเต็มตัวที่ 1: ");
            int num1 = scanner.nextInt();

            // รับข้อมูลจำนวนเต็มตัวที่ 2
            System.out.print("กรุณาใส่จำนวนเต็มตัวที่ 2: ");
            int num2 = scanner.nextInt();

            // คำนวณผลรวม
            int result = add(num1, num2);

            // แสดงผลลัพธ์
            System.out.println("ผลบวกของ " + num1 + " กับ " + num2 + " คือ " + result);

        } catch (Exception e) {
            System.out.println("กรุณาใส่ข้อมูลเป็นจำนวนเต็มเท่านั้น!");
        } finally {
            scanner.close();
        }
    }

    // เมธอดสำหรับบวกเลข 2 ตัว
    public static int add(int a, int b) {
        return a + b;
    }
}