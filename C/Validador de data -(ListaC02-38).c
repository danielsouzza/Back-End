#include<stdio.h>
#include<string.h>

/* Funções*/
char verify_year(int x);
void verify(int x, int y, int z);

/*Função principal*/
int main() {

    int day, month, year;
    printf("Digite uma data: ");
    scanf("%d %d %d", &day, &month, &year);

    verify(month, year, day);

    return 0;
}

/* Verificar se o ano é bissexto*/
char verify_year(int y) {
    int result;

    if(y % 400 == 0 || y % 4 == 0 && !(y % 100 == 0))
        result = 1;

    else
        result = 2;
    return(result);
}
/* validação principal*/
void verify(int m, int y, int d) {
    int result;
    if(y <= 2022) {
        if(m > 0 && m <= 12) {
            if(m == 1|| m == 3||m == 5||m == 7||m == 8||m == 10||m == 12) {
                if(d > 0 && d <= 31)
                    printf("\nA data %d/%d/%d é válida", d, m, y);
            }

            else if(m == 2) {
                result = verify_year(y);
                if(result == 1) {
                    if(d > 0 && d <= 29)
                        printf("\nA data %d/%d/%d é válida", d, m, y);
                }

                else if(result == 2) {
                    if(d > 0 && d <= 28)
                        printf("\nA data %d/%d/%d é válida", d, m, y);
                    else
                        printf("\nA data %d/%d/%d é inválida", d, m, y);
                }

            }

            else if(d > 0 && d <= 30)
                printf("\nA data %d/%d/%d é válida", d, m, y);

            else
                printf("\nA data %d/%d/%d é inválida", d, m, y);
        }
        else
            printf("O mês %d não atende o limite de meses padrão", m);
    }
    else
        printf("O ano %d não é válido", y);
}