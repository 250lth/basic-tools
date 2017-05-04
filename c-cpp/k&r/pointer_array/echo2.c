//
// Created by lth on 17-5-4.
//

#include <stdio.h>

int main(int argc, char *argv[]) {
    while (--argc > 0)
        printf("%s%s", *++argv, (argc > 1) ? " " : "");
    printf("\n");
    return 0;
}