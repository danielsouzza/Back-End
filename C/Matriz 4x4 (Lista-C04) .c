#include<stdio.h>

int main()
{
    int matriz[4][4];
    int i, j;

    printf("Digite os valores da matriz 4 x 4: \n");
    for(i = 0; i < 4; i++) {
        for(j = 0; j < 4; j++) {
            scanf("%d", &matriz[i][j]);
        }
    }
    printf(" Matriz 4x4:");
    for(i = 0; i < 4; i++) {
        printf("\n");
        for(j = 0; j < 4; j++) {
            printf(" %d ", matriz[i][j]);
        }
    }
    return 0;
}