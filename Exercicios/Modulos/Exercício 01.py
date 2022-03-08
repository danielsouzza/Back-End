from utilidades import moeda
from utilidades import dado

value = dado.leiadinheiro("Digite o valor: R$")
moeda.resumo(value, 80, 35)