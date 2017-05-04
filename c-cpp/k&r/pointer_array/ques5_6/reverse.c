//
// Created by lth on 17-5-4.
//

#include <string.h>

void reverse(char *s) {
    int c;
    char *t;

    for (t = s + (strlen(s) - 1); s < t; s++, t--) {
        c = *s;
        *s = *t;
        *t = c;
    }
}