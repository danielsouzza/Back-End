# tratamento de erro para números int e float
def leianum(msg,tipo):
    num = 0
    while True:
        try:
            if tipo == "i":
                valor = int(input(msg))
            elif tipo == "r":
                valor = float(input(msg))
        except (ValueError, TypeError):
            if tipo == "i":
                print(f"\033[0;31mErro: por favor, digite um número inteiro válido \033[m")
            if tipo == 'r':
                print(f"\033[0;31mErro: por favor, digite um número real válido \033[m")
        except (KeyboardInterrupt):
            if tipo == "i":
                print(f"\033[0;31mErro: por favor, digite um número inteiro válido \033[m")
            if tipo == 'r':
                print(f"\033[0;31mErro: por favor, digite um número real válido \033[m")
            continue
        else:
            return valor


#programa principal
def main():
    inteiro = leianum("Digite um número inteiro: ",'i')
    real = leianum("Digite um número real: ",'r')
    print(f"Valor inteiro:\t{inteiro}")
    print(f"Valor real:\t{real}")
main()