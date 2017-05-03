//
// Created by lth on 17-5-3.
//

#include <stdio.h>

unsigned invert(unsigned x, int p, int n) {
    return x ^ (~(~0 << n) << (p + 1 - n));
}

int main() {
    printf("%u", invert(423413, 3, 5));
}
