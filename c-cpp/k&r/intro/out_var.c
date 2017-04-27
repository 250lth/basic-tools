//
// Created by lth on 17-4-27.
//

#include <stdio.h>

#define MAXLINE 100

int max;
char line[MAXLINE];
char longest[MAXLINE];

int get_line(void);
void copy(void);

int main() {
    int len;
    extern int max;
    extern char longest[MAXLINE];

    max = 0;
    while ((len = get_line()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)
        printf("%s", longest);
    return 0;
}

int get_line(void) {
    int c, i;
    extern char line[MAXLINE];

    for (i = 0; i < MAXLINE-1 && (c = getchar()) != EOF && c != '\n'; ++i)
        line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

void copy(void) {
    int i;
    extern char line[MAXLINE], longest[MAXLINE];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}