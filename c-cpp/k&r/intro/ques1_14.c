//
// Created by lth on 17-4-27.
//

#include <stdio.h>

#define MAXHIST 15
#define MAXWORD 11
#define IN 1
#define OUT 0

int main() {
    int c, i, j, nc, state;
    int maxValue;
    int ovflow;
    int wl[MAXWORD];
    state = OUT;
    nc = 0;
    ovflow = 0;
    for (i = 0; i < MAXWORD; ++i)
        wl[i] = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
            if (nc > 0)
                if (nc < MAXWORD)
                    ++wl[nc];
                else
                    ++ovflow;
            nc = 0;
        } else if (state == OUT) {
            state = IN;
            nc = 1;
        } else
            ++nc;
    }

    maxValue = 0;

    for (i = 1; i < MAXWORD; ++i)
        if (wl[i] > maxValue)
            maxValue = wl[i];

    for (i = MAXHIST; i > 0; --i) {
        for (j = 1; j < MAXWORD; ++j)
            if (wl[j] * MAXHIST / maxValue >= i)
                printf(" * ");
            else
                printf("   ");
        putchar('\n');
    }

    for (i = 1; i < MAXWORD; ++i)
        printf("%4d ", i);
    putchar('\n');

    for (i = 1; i < MAXWORD; ++i)
        printf("%4d ", wl[i]);
    putchar('\n');

    if (ovflow > 0)
        printf("There are %d words >= %d\n", ovflow, MAXWORD);

    return 0;
}