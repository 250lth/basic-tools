//
// Created by lth on 17-4-24.
//

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    char *myenv[] = {"JUICE=peach and apple", NULL};
    execle("diner_info", "diner_info", "4", NULL, myenv);
    printf("Diners: %s\n", argv[1]);
    printf("Juice: %s\n", getenv("JUICE"));
    return 0;
}