"""
Alguns dos meus primeiros exercicios em python.

Rode cada um separadamente!!
"""
#Variáves e expressões

# Suma de 3 números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
t = (n1 + n2 + n3)
print(f'A soma é igual a: {t}')

# Conversor de temperatura de celsius para fahrenheit
tc = float(input('Digite a temperatura em celsius: '))
f = tc * (9.0/5.0)+32.0
print(f'A temperatura em fahrenheit : {f} ')

# Aumnto de 25% dado um salário
n = input('Name: ')
s = int(input('Salário: R$'))
s = s + (25/100 * s)
print(f'Salário com 25% de aumento: R${s}')

# Contador de salário com 10% de aumento 
vh = int(input('Valor da hora: R$'))
qt = int(input('Quantidade de horas: '))
salario = vh * qt * 26
salario = salario + (10/100 * salario)                        
print(f'Salário do funcionario: R${salario}')

#05 Leitor de números 
num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

#06 Tempo de um experimento
horario_i = int(input('Horário de inicio do experimento em segundos: '))
h_i = horario_i // 3600
r_i = horario_i % 3600
m_i = r_i // 60
s_i = r_i % 60
print(f'Inicio do experimento: {h_i:.0f}:{m_i:.0f}:{s_i}.pm')

horario_d = int(input('Tempo de deduração do experimento em segundos: '))
h_d = horario_d // 3600
r_d = horario_d % 3600
m_d = r_d // 60
s_d = r_d % 60
print(f'Tempo de duração do experimento: {h_d:.0f}:{m_d:.0f}:{s_d}')

horario_f = horario_i + horario_d
h_f = horario_f // 3600
r_f = horario_f % 3600
m_f = r_f // 60
s_f = r_f % 60
print(f'Horário do termino do experimento: {h_f:.0f}:{m_f:.0f}:{s_f}.pm')

#07 Orçamento para cerca um terreno 
c = int(input('Digite o comprimento do terreno: '))
l = int(input('Digite a largura do terreno: '))
pt = float(input('Valor do metro tela: R$'))
p = (2 * c) + (2 * l)
v = pt * p
print(f'O custo para certa o terreno é R${v:.0f}')