# Gerador de numeros primos
def prime(x=0,y=0):
    for i in range(x,y+1):
        primo = 0
        for j in range(1,i+1):
            if i % j == 0:
                primo += 1
        if primo == 2:
            yield i


def entrada(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[0;31mErro: por favor, digite um número inteiro válido \033[m")
            continue
        else:
            return valor

def main():
    st = entrada("Digite o número inicial: ")
    fn = entrada("Digite o número final: ")
    print(f"Os número primo no intervalo de {st} e {fn} são:")
    for i in prime(st, fn):
        print(i,end=" => ")
    print(" fim\n")
main()