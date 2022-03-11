# Detalhe
def divi():
    print("="*50)

# formatação do menu
def cabeçalho(text):
    divi()
    print(text.center(42))
    divi()

# Mostra as opções na tela
def menu(lista):
    cabeçalho("Menu Principal")
    num = 1
    for item in lista:
        print(f"{num} - {item}")
        num += 1
    divi()

# Verificar se é inteiro/coreespondente a uma opção 
def entrada(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[0;31mErro: por favor, digite um número inteiro válido \033[m")
            continue
        if valor not in range(1,4):
            print(f"\033[0;31mErro: opção inválida \033[m")
            continue
        else:
            return valor
