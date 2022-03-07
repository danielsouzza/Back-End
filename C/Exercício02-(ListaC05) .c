#include<stdio.h>

int main()
{
    char world[10];
    int i, count = 0;
    
    printf("Digite uma palavra: ");
    gets(world);
    for(i = 0; world[i] != '\0'; i++){
        count++;
    }
    printf("A palavra: %s\ntamanho: %d", world, count);
    return 0;
}