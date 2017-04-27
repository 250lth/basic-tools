//
// Created by lth on 17-4-27.
//

#include <stdio.h>

#define NONBLANK 'a'

int main() {
    int c, lastc;

    lastc = NONBLANK;
    while ((c = getchar()) != EOF) {
        if (c != ' ' || lastc != ' ')
            putchar(c);
        lastc = c;
    }

    return 0;
}