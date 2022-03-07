"""
Alguns dos meus primeiros exercicios em python.

Rode cada um separadamente!!
"""
#Comando de repetição

# Quantidade de números/vezes que aparece
usuario = int(input('Digite quantidade de números:  '))
lista = list()
for i in range(usuario):
    num = int(input('Digite um valor: '))
    lista.append(num)
maior = max(lista)
vezes = lista.count(maior)
print(f'O maior número foi {maior} e ele repetiu {vezes}')

# Determinar se é par ou não 
cont = 0
pares = list()
print('DIGITE 1000 PARA STOP')
num = int(input('Digite um valor'))
while num != 1000:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)
    cont += 1
print(f'Foram informados {cont} números e {len(pares)} são pares')

# Contagem regressiva 
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('BOOM, BOOW, POOW')

# Calculadora de multiplicação
num = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{num} x {i} = {i * num}')

# Termos de uma PA
from time import sleep
print('='* 25)
print('10 TERMOS DE UM PA')
print('='* 25)
t1 = int(input('Primeiro termo: '))
rz = int(input('Razão:'))
print('='* 25)
for i in range(t1, 10):
    mult = i * rz
    sleep(1)
    print(f'{mult}' ,end='=> ')
print('ACABOU!!')

# Características de um grupo
name = list()
man = list()
women = list()
idades = list()
for i in range(1, 5):
    print(f'========= {i}ª pessoa =======')
    nome = input('Nome: ').strip().upper()
    name.append(nome)
    
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = input('Sexo[M/F]: ').upper()
    
    if sexo == 'M':
        man.append(idade)
    else:
        if sexo == 'F' and idade  < 20:
            women.append(idade)
print(f'A média de idade do grupo é {sum(idades) / len(idades) }')
print(f'O homen mais velho tem {max(man)} e se chama {name[man.index(max(man))]}')
print(f'Tem {len(women)} mulheres com menos de 20 anos')

# Registrador de sexo
sexo = input('Informe seu sexo[M/F]: ').upper()
while sexo not in ('F','M'):
    print('Sexo inválido !!')
    sexo = input('Informe seu sexo[M/F]: ').upper()
print(f'Sexo {sexo} foi registrado com sucesso')

# Game de adivinhação 
from random import randint
IA = randint(1,11)
cont = 1
print(f'Olá, pensei em um númro, você consegui adivinhar?')
player = int(input('Que número é esse?\n'))
while player != IA:
    if player < IA:
        player = int(input('Mais...Tente novamente:\n'))
    else:
        if player > IA:
            player = int(input('Menos...Tente novamente:\n'))
    cont += 1
print(f'Você acetou com {cont} tentativas. Parebéns!')

# Gerador de PA 2.0
from time import sleep
print('GERADOR DE PA')
print('='*15)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termo = pt
i = 1
while i <= 10:
    sleep(1)
    print(f'{termo}',end=' => ')
    termo += rz
    i += 1
print('PAUSOU!!')
nt = 10
q = 1
while q != 0:
    q = int(input('\nQuantos termos você quer mostra a mais? '))
    c = 1
    while c <= q:
        sleep(1)
        print(f'{termo}',end=' => ')
        termo += rz
        c += 1
        nt += 1
    print(f'PAUSOU!!')
print(f'Pregressão finalizada com {nt} termos mostrados')