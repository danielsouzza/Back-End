from time import sleep
from lib.data import * # Manipulação do arquivo
from lib.interface import * # Criação do menu

def main():
    # Arquivo a ser cridado
    file = "Exercicios/cadastro/lib/data/data center.txt"
    # Verificar se o arquivo já exste
    if not arquivo(file):
        criararq(file)
    # Opções a ser mostrada
    options = ['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema']
    menu(options)

    while True:
        # Interação com o usuário
        choice = entrada("\033[33mSua opção:>_ \033[m")
        # Mostrar pessoas cadastradas
        if choice == 1:
            cabeçalho("PESSOAS CADASTRADAS")
            readfile(file)
        # Cadastra uma nova pessoa
        elif choice == 2:
           cabeçalho("NOVO CADASTRO")
           name = input("Nome: ")
           age = input("Idade: ")
           cadastro(file, name, age)
        # finalizar o programa
        elif choice == 3:
            cabeçalho(f"Saindo do sistema ... Até logo!!")
            break
        sleep(0.1)
main()