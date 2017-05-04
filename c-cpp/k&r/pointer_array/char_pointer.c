//
// Created by lth on 17-5-4.
//

/**
 * Ways of implementing strcpy
 * @param s
 * @param t
 */
void strcpy1(char *s, char *t) {
    int i;

    i = 0;
    while ((s[i] = t[i]) != '\0')
        i++;
}

void strcpy2(char *s, char *t) {
    while ((*s = *t) != '\0') {
        s++;
        t++;
    }
}

void strcpy3(char *s, char *t) {
    while ((*s++ - *t++) != '\0')
        ;
}

void strcpy4(char *s, char *t) {
    while (*s++ = *t++)
        ;
}


/**
 * Ways of implementing strcmp
 * @param s
 * @param t
 * @return
 */
int strcmp1(char *s, char *t) {
    int i;
    for (i = 0; s[i] == t[i]; i++)
        if (s[i] == '\0')
            return 0;
    return s[i] - t[i];
}

int strcmp2(char *s, char *t) {
    for (; *s == *t; s++, t++)
        if (*s == '\0')
            return 0;
    return *s - *t;
}

