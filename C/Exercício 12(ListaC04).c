#include<stdio.h>

int main()
{
    int vetor[4];
    int i, maior, menor;
    float media;
    maior = menor = media = 0;
    
    printf("Digite 5 valores: \n");
    for(i = 0; i <= 4; i++){
        scanf("%d", &vetor[i]);
        media += vetor[i];
        if(i == 0)
            maior = menor = vetor[i];
        if(vetor[i] > maior)
            maior = vetor[i];
        if(vetor[i] < menor)
            menor = vetor[i];
    }
    media = media / 5;
    
    printf("Maior número = %d\n", maior);
    printf("Menor número = %d\n", menor);
    printf("A média é = %4.2f\n", media);
    
    return 0;
}