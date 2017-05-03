//
// Created by lth on 17-5-3.
//

#include <stdio.h>

unsigned rightrot(unsigned x ,int n) {
    int wordlength;
    int rbit;

    while (n-- > 0) {
        rbit = (x & 1) << (wordlength - 1);
        x = x >> 1;
        x = x | rbit;
    }
    return x;
}

int main() {
    printf("%u", rightrot(1311314, 2));
}