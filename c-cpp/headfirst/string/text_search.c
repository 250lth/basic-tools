//
// Created by lth on 17-4-21.
//

#include <stdio.h>
#include <string.h>

char tracks[][80] = {
        "I left my heart in Harvard Med School",
        "Newark, Newark - a wonderful town",
        "Dancing with a Dork",
        "From here to maternity",
        "The girl from Iwo Jima"
};

void find_track(char search_for[]) {
    int i;
    for (i = 0; i < 5; i++) {
        if (strstr(tracks[i], search_for))
            printf("Track %i: '%s'\n", i, tracks[i]);
    }
}

int main3a() {
    char search_for[80];
    printf("Search for: ");
    fgets(search_for, 80, stdin);
    search_for[strlen(search_for)-1] = '\0';
    find_track(search_for);
    return 0;
}