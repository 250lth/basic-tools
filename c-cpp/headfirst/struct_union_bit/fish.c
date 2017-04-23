//
// Created by lth on 17-4-23.
//
#include <stdio.h>

struct preferences {
    const char *food;
    float exercise_hours;
};

struct fish {
    const char *name;
    const char *species;
    int teeth;
    int age;
    struct preferences care;
};

void catalog(struct fish f) {
    printf("%s is a %s with %i teeth. He is %i\n",
        f.name, f.species, f.teeth, f.age);
}

int main5a() {
    struct fish snappy = {"Snappy", "piranha", 69, 4, {"Meat", 7.5}};
    catalog(snappy);
    printf("Snappy likes to eat: %s. ", snappy.care.food);
    printf("Snappy likes to exercise %f hours. ", snappy.care.exercise_hours);
    return 0;
}