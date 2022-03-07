#include<stdio.h>

int main()
{
    int matriz[5][5] = {
       {1, 2, 3, 4, 5},
       {3, 4, 7, 8, 9},
       {4, 6, 8, 9, 5},
       {5, 8, 8, 3, 9},
       {1, 8, 7, 5, 2}
    };
    int i, j;

    for(i = 0; i <= 4; i++) {
        for(j = 0; j <= 4; j++) {
            if(i == j) {
                matriz[i][j] = 1;
            } else {
                matriz[i][j] = 0;
            }

        }
    }
    printf(" Matriz 5x5:");
    for(i = 0; i <= 4; i++) {
        printf("\n");
        for(j = 0; j <= 4; j++) {
            printf(" %d ", matriz[i][j]);
        }
    }
    return 0;
}