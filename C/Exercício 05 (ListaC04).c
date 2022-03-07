#include<stdio.h>

int main()
{
    int vetor[9];
    int i, count;
    
    printf("Digite 10 números: \n");
    for(i = 0; i <= 9; i++){
        scanf("%d", & vetor[i]);
        if(vetor[i] % 2 == 0){
            count++;
        }
    }
    printf("Foram digitados %d números pares.", count);
    
    return 0;
}