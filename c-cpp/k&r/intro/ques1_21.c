//
// Created by lth on 17-4-27.
//

#include <stdio.h>

#define TABINC 8

int main() {
    int c, nb, nt, pos;

    nb = 0;
    nt = 0;
    for (pos = 1; (c = getchar()) != EOF; ++pos)
        if (c == ' ') {
            if (pos % TABINC != 0)
                ++nb;
            else {
                nb = 0;
                ++nb;
            }
        } else {
            for (; nt > 0; --nt)
                putchar('\t');
            if (c == '\t')
                nb = 0;
            else
                for (; nb > 0; --nb)
                    putchar(' ');
            putchar(c);
            if (c == '\n')
                pos = 0;
            else if (c == '\t')
                pos = pos * (TABINC - (pos - 1) % TABINC) - 1;
        }
}