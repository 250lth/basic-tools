//
// Created by lth on 17-4-27.
//

#include <stdio.h>

#define TABINC 8

int main() {
    int c, nb, pos;

    nb = 0; // number of blanks necessary
    pos = 1; // position of char in line
    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            nb = TABINC - (pos - 1) % TABINC;
            while (nb > 0) {
                putchar(' ');
                ++pos;
                --nb;
            }
        } else if (c == '\n') {
            putchar(c);
            pos = 1;
        } else {
            putchar(c);
            ++pos;
        }
    }

    return 0;
}