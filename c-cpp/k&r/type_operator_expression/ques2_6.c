//
// Created by lth on 17-5-3.
//
#include <stdio.h>

unsigned setbits(unsigned x, int p, int n, unsigned y) {
    return x & ~(~(~0 << n) << (p + 1 - n)) | (y & ~(~0 << n)) << (p + 1 - n);
}

int main() {
    printf("%u", setbits(4342423, 3, 4, 425416));
}