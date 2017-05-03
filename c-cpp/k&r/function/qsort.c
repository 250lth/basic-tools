//
// Created by lth on 17-5-3.
//

#include <stdio.h>

void qsort(int v[], int left, int right);
void swap(int v[], int i, int j);

int main() {
    int v[] = {3,1,4,5,63,2,4,2,1,9};
    qsort(v, 0, 9);
    for (int i = 0; i <= 9; ++i) {
        printf("%d ", v[i]);
    }
    printf("\n");
}

void qsort(int v[], int left, int right) {
    int i, last;
    void swap(int v[], int i, int j);

    if (left >= right)
        return;
    swap(v, left, (left + right) / 2);
    last = left;
    for (i = left + 1; i <= right; i++)
        if (v[i] < v[left])
            swap(v, ++last, i);
    swap(v, left, last);
    qsort(v, left, last - 1);
    qsort(v, last + 1, right);
}

void swap(int v[], int i, int j) {
    int temp;

    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}