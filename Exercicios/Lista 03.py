"""
Alguns dos meus primeiros exercicios em python.

Rode cada um separadamente!!
"""
#Comando condicionais

# Maior número
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print(f'O maior número é {n1}')
elif n2 > n1:
    print(f'O maior númro é {n2}')

# Liberação de empréstimo
salario = int(input('Valor do salário: R$'))
p = int(input('Valor da prestação: R$'))
if p > (20/100 * salario):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido ')

# Peso ideal
altura = float(input('Digite a altura: '))
sexo = input('Digite seu sexo: ')
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) -44.7
if sexo == 'homem':
    print(f'Seu peso ideal é {homem:.2f}kg')
elif sexo == 'mulher':
    print(f'Seu peso ideal é {mulher:.2f}kg')

# Calcular média de nota
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (2*n1 + 3*n2 + 5*n3) /10  # Mádia ponderada
print(f'média: {m:.1f}')
if (m == 0 or m <= 2.9):
    print('Aluno reprovado')
elif (m == 3 or m <= 4.9):
    print('Aluno  está de recuperação')
elif m >= 5:
    print('Aluno aprovado')

# Calculadora basica
print('  ============[Escolha o tipo de operação matemática]============')
menu = input('Adição, subtração, multiplicação ou divisão: \n')
if menu == 'Adição':
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro número: '))
    print(f'{n1} + {n2} = {n1+n2}')
elif menu == 'Subtração':
    n1 = int(input('Digite um númro: '))
    n2 = int(input('Digite putro número: '))
    print(f'{n1} - {n2} = {n1-n2}')
elif menu == 'Multiplicação':
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número: '))
    print(f'{n1} x {n2} = {n1*n2}')
elif menu == 'Divisão':
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(f'{n1} / {n2} = {n1/n2}')

#  multiplo de 3 e 5
n = int(input('Digite um número: '))
if (n % 3 == 0) and (n % 5 == 0):
    print(f'Esse número é divisível por 3 e por 5 ')
elif (n % 3 == 0):
    print(f'{n} é dividível por 3')
elif (n % 5 == 0):
    print(f'{n} é divisível por 5')
else:
    print('Esse número não é divisível por 3 e nem por 5')

# Verificar tipo de Triângulo
a = int(input('Informe um valor: '))
b = int(input('Informe outro valor: '))
c = int(input('Informe mais um valor: '))
if (a > b + c) or (b > a + c) or (c > a + b):
    print('Não é um triângulo')
elif (a == b == c):
    print('Um triângulo equilátero')
elif (a == b) ^ (b == c) ^ (a == c):
    print('UM triângulo isósceles')
elif (a != b) and (b != c) and (a != c):
    print('Um triângulo escaleno')

# Condições para aposentadoria
idade = int(input('Informe sua idade: '))
tempo = int(input('Informe o tempo de trabalho: '))
if idade >= 65 or tempo >= 30 or idade >= 60 and tempo >=25:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')

# Diferençã de imposto por estado
valor = int(input('Informe um valor do produto: R$'))
estado = input('Digite o estado destino: ')
mg = valor + ( 7/100 * valor)
sp = valor + (12/100 * valor)
rj = valor + (15/100 * valor)
ms = valor + ( 9/100 * valor)
if estado == 'MG':
    print(f'O valor com 7% de imposto é R${mg}')
elif estado == 'SP':
    print(f'O valor com 12% de imposto é R${sp}')
elif estado =='RJ':
    print(f'O valor com 15% de imposto é R${rj}')
elif estado == 'MS':
    print(f'O valor com 9% de imposto é R${ms}')
else:
    print('Informações inválidas')

# Game Pedra, papel e tesoura
from random import randint
from time import sleep
print("""Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
I = int(input('Qual é sua jogada: '))
lista = ['JO', 'KEN', 'PO!!']
for i in lista:
    print(i)
    sleep(1)
IA = randint(0,2)
itens = ('pedra', 'papel','tesoura')
print('-= ' * 11)
print(f'A IA jogou {itens[IA]}')
print(f'O jogador jogou {itens[I]}')
print('-=' * 11)

if I == 0 and IA == 0 or I == 1 and IA == 1 or I == 2 and IA == 2:
    print('O jogo empatou !!')
elif I == 0 and IA == 1 or I == 1 and IA == 2 or I == 2 and IA == 0:
    print('Jogador perdeu !!')
elif I == 1 and IA == 2 or I == 2 and IA == 1 or I == 1 and IA == 0:
    print('Jogador Venceu !!')

# Palíndromo
name = str(input('Digite uma palavra: ')).strip().upper()
frase = name.split()
junto = ''.join(frase)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Essa palavra é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo!')