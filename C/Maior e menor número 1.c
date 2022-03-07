#include<stdio.h>

int main() {
    int n0;
    int n1;

    printf("Type two numbers to see which and the longe number");
    printf("\nEnter first number: ");
    scanf("%d", &n0);

    printf("\nEnter second number: ");
    scanf("%d", &n1);

    if(n0 > n1)
        printf("%d is the langer number", n0);
    else
        printf("%d is the langer number", n1);


    return 0;
}