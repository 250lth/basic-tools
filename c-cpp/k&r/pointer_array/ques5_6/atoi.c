//
// Created by lth on 17-5-4.
//

#include <ctype.h>

int atoi(char *s) {
    int n, sign;

    for (; isspace(*s); s++)
        ;
    sign = (*s == '-') ? -1 : 1;
    if (*s == '+' || *s == '-')
        s++;
    for (n = 0; isdigit(*s); s++)
        n = 10 * n + *s - '0';

    return sign * n;
}