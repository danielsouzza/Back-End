#include<stdio.h>
#include<string.h>


int main()
{
    char alpha[] = {"abcdefghijklmnopqrstuvwxyz"};
    char alpharev[] = {"zyxwvutsrqponmlkjihgfedcba"};
    char user[50], cript[100];
    int i, k;

    printf("Digite uma mensagem: \n     ");
    gets(user);

    for(k = 0; user[k] != '\0'; k++) {
        for(i = 0; alpha[i] != '\0'; i++) {
            if(alpha[i] == user[k]) {
                cript[k] = alpharev[i];
            } else {
                if(user[k] == ' ')
                    cript[k] = ' ';
            }
        }
    }


    printf("   Mensagem original\n");
    printf("     %s    \n", user);
    printf("Mensagem criptografada\n");
    printf("     %s    \n", cript);

    return 0;
}
