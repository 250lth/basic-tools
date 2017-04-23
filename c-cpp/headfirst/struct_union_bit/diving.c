//
// Created by lth on 17-4-23.
//

#include <stdio.h>

typedef struct {
    float tank_capicity;
    int tank_psi;
    const char *suit_material;
} equipment;

typedef struct scuba {
    const char *name;
    equipment kit;
} diver;

void badge(diver d) {
    printf("Name: %s Tank: %2.2f(%i) Suit: %s\n",
        d.name, d.kit.tank_capicity, d.kit.tank_psi, d.kit.suit_material);
}

int main5b() {
    diver randy = {"Randy", {5.5, 3500, "Neoprene"}};
    badge(randy);
    return 0;
}