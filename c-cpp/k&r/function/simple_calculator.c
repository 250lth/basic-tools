//
// Created by lth on 17-5-3.
//

#include <stdio.h>

#define MAXLINE 100

int main() {
    double sum, atof(char[]);
    char line[MAXLINE];
    int getlines(char line[], int max);

    sum = 0;
    while (getlines(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}