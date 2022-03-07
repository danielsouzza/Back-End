#include<stdio.h>

int main()
{
    int vetor[] = {2,5,4,9,8,7,6,1};
    int x, y, soma;
    
    printf("Digite duas posição entre [0 e 7]: \n");
    scanf("%d\n%d", &x, &y);
    soma = vetor[x] + vetor[y];
    printf("Soma de %d + %d = %d", vetor[x], vetor[y], soma);
    return 0;
}