#include<stdio.h>

int main()
{
    int A[5];
    int i, soma;
    
    //Atribuir valores:
    for(i = 0; i <= 5; i++){
        printf("Número %d : ", i+1);
        scanf("%d", &A[i]);
    }
    
    //Soma dos elementos A[0], A[1] e A[5]:
    soma = (A[0] + A[1] + A[5]);
    printf("\nA soma dos elementos A[0], A[1] e A[5] é = %d", soma);
    
    //Modificação de elemento A[4]:
    A[4] = 100;
    
    // print de todos os elementos de A:
    printf("\nTodos os elementos:");
    for(i = 0; i <= 5; i++)
        printf("\n  %d", A[i]);
    
    return 0;
}