//
// Created by lth on 17-4-24.
//

#include <stdio.h>
#include <unistd.h>
#include <error.h>
#include <string.h>

int main() {
    if (execl("/sbin/ifconfig", "/sbin/ifconfig", NULL) == -1)
        if (execlp("ipconfig", "ipconfig", NULL) == -1) {
            fprintf(stderr, "Cannot run ipconfig: %s", strerror(error));
            return 1;
        }
    return 0;
}