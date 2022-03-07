#include<stdio.h>

int main()
{
    int i, A[10];
    int k, B[10];
    
    for(i = 0; i<= 9; i++){
        scanf("%d", &A[i]);
        B[i] = A[i] * A[i];
    }
    for(k = 0; k <= 9; k++){
        printf("%d ", A[k]);
    }
    printf("\n");
    for(k = 0; k <= 9; k++)
        printf("%d ", B[k]);
    return 0;
}