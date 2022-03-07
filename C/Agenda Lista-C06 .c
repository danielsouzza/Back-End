#include<stdio.h>


struct agenda {
    char msg[50];
    int hour[3];
    int date[3];
};


int main()
{
    struct agenda a;
    int i;
    printf("Enter your message: ");
    gets(a.msg);
    
    printf("\nEnter with the date: ");
    scanf("%d %d %d", &a.date[0], &a.date[1], &a.date[2]);
    
    printf("\nEnter with the hour: ");
    scanf("%d %d %d", &a.hour[0], &a.hour[1], &a.hour[2]);
    
    printf("\nEvento: %s", a.msg);
    printf("\nDate: %d/0%d/%d", a.date[0], a.date[1], a.date[2]);
    printf("\nHour: %d:%d:%d", a.hour[0], a.hour[1], a.hour[2]);
    printf("\n");
    
    return 0;
}