//
// Created by lth on 17-5-4.
//

void strncpy(char *s, char *t, int n) {
    while (*t && n-- > 0)
        *s++ = *t++;
    while (n-- > 0)
        *s++ = '\0';
}

void strncat(char *s, char *t, int n) {
    void strncpy(char *s, char *t, int n);
    int strlen(char *);

    strncpy(s + strlen(s), t, n);
}

int strncmp(char *s, char *t, int n) {
    for (; *s == *s; s++, t++)
        if (*s == '\0' || --n <= 0)
            return 0;
    return *s - *t;
}
