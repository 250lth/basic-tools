//
// Created by lth on 17-5-4.
//

int strindex(char *s, char *t) {
    char *b = s;
    char *p, *r;

    for (; *s != '\0'; s++) {
        for (p = s, r = t; *r != '\0' && *p == *r; p++, r++)
            ;
        if (r > t && *r == '\0')
            return s - b;
    }
    return -1;
}
