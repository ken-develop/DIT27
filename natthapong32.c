#include <stdio.h>

int main() {
    int num1, num2, sum;

    
    printf("กรุณาใส่จำนวนเต็มตัวแรก: ");
    scanf("%d", &num1);

    printf("กรุณาใส่จำนวนเต็มตัวที่สอง: ");
    scanf("%d", &num2);
    
    sum = num1 + num2;

    printf("ผลบวกของ %d และ %d คือ: %d\n", num1, num2, sum);

    return 0;
}
