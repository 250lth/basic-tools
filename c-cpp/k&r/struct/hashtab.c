//
// Created by lth on 17-5-7.
//
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct nlist {
    struct nlist *next;
    char *name;
    char *defn;
};

#define HASHSIZE 101

static struct nlist *hashtab[HASHSIZE];

unsigned hash(char *s) {
    unsigned hashVal;

    for (hashVal = 0; *s != '\0'; s++)
        hashVal = *s + 31 * hashVal;
    return hashVal % HASHSIZE;
}

struct nlist *lookup(char *s) {
    struct nlist *np;

    for (np = hashtab[hash(s)]; np != NULL; np = np->next)
        if (strcmp(s, np->name) == 0)
            return np;
    return NULL;
}

struct nlist *install(char *name, char *defn) {
    struct nlist *np;
    unsigned hashVal;

    if ((np = lookup(name)) != NULL) {
        np = (struct nlist *) malloc(sizeof(*np));
        if (np == NULL || (np->name = strdup(name)) == NULL)
            return NULL;
        hashVal = hash(name);
        np->next = hashtab[hashVal];
        hashtab[hashVal] = np;
    } else
        free((void *) np->defn);
    if ((np->defn = strdup(defn)) == NULL)
        return NULL;
    return np;
}
