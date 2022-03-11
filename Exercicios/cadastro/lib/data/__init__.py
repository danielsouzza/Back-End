from lib.interface import *

# verificar se o arquivo já existe
def arquivo(file):
    try:
        file = open(file, "rt")
        file.close()
    except (FileNotFoundError):
        return False
    else:
        return True
# cria o arquivo
def criararq(file):
    try:
        arq = open(file, "wt+")
    except:
        print("Hove um erro na criação do arquivo")
    else:
        print("\n")
        print(f"    Arquivo (data center.txt) criado com sucesso")
        arq.close()

# Realizar o cadastro 
def cadastro(arq, name="desconhecido", age=0):
    try:
        arq = open(arq, "at")
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            arq.write(f"{name};{age}\n")
        except:
            print("Ocorreu um erro ao escrever os dados")
        else:
            cabeçalho(f"{name} foi cadastrada com sucesso!!")
        finally:
            arq.close()

# Ler e mostra as pessoas cadastradas
def readfile(file):
    try:
        arq = open(file, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        for line in arq:
            dado = line.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        divi()
        arq.close()
