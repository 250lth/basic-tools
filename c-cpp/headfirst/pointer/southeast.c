//
// Created by lth on 17-4-21.
//
#include <stdio.h>

void go_south_east(int* lat, int* lon) {
    *lat = *lat - 1;
    *lon = *lon + 1;
}

int main2a() {
    int latitude = 32;
    int longitude = -64;

    go_south_east(&latitude, &longitude);

    printf("Stop! The current location is: [%i, %i]\n", latitude, longitude);

    return 0;
}
