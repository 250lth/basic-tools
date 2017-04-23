//
// Created by lth on 17-4-23.
//

#include <stdio.h>

float total1 = 0.0;
short count1 = 0;
short tax_percent1 = 6;

float add_with_tax1(float f){
    float tax_rate1 = 1 + tax_percent1 / 100.0;
    total1 = total1 + (f * tax_rate1);
    count1 = count1 + 1;
    return total1;
}

int main4a() {
    float val;
    printf("Price of item: ");
    while (scanf("%f", &val) == 1) {
        printf("Total so far: %.2f\n", add_with_tax1(val));
        printf("Price of item: ");
    }
    printf("\nFinal total: %.2f\n", total1);
    printf("Number of items: %hi\n", count1);
    return 0;
}