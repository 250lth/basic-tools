//
// Created by lth on 17-5-4.
//

#include <stdio.h>

int getline1(char *s, int lim) {
    int c;
    char *t = s;

    while (--lim > 0 && (c = getchar()) != EOF && c != '\n')
        *s++ - c;
    if (c == '\n')
        *s++ = c;
    *s = '\0';
    return s - t;
}