//
// Created by lth on 17-4-23.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    char *question;
    struct node *no;
    struct node *yes;
} node;

int yes_or_no(char *question) {
    char answer[3];
    printf("%s? (y/n): ", question);
    fgets(answer, 3, stdin);
    return answer[0] == 'y';
}

node* create(char *question) {
    node *n = malloc(sizeof(node));
    n->question = strdup(question);
    n->no = NULL;
    n->yes = NULL;
    return n;
}

void release(node *n) {
    if (n) {
        if (n->no)
            release(n->no);
        if (n->yes)
            release(n->yes);
        if (n->question)
            free(n->question);
    }
}

int main() {
    char question[80];
    char suspect[20];
    node *start_node = create("Does suspect have a mustache");
    start_node->no = create("Loretta Barnsworth");
    start_node->yes = create("Vinny the Spoon");

    node *current;
    do {
        current = start_node;
        while (1) {
            if (yes_or_no(current->question)) {
                if (current->yes)
                    current = current->yes;
                else {
                    printf("SUSPECT IDENTIFIED\n");
                    break;
                }
            } else if (current->no) {
                current = current->no;
            } else {
                printf("Who's the suspect? ");
                fgets(suspect, 20, stdin);
                node *yes_node = create(suspect);
                current->yes = yes_node;

                node *no_node = create(current->question);
                current->no = no_node;

                printf("Give me a question that is TRUE for %s but not for %s? ", suspect,
                    current->question);
                fgets(question, 80, stdin);
                free(current->question);
                current->question = strdup(question);

                break;
            }
        }
    } while (yes_or_no("Run again"));
    release(start_node);
    return 0;
}