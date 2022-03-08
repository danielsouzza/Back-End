# Metade do valor
def metade(value=0, formato=False):
    met = value / 2
    return met if formato is False else moeda(met)


#Dobro do valor
def dobro(value=0, formato=False):
    rst = value * 2
    return rst if formato is False else moeda(rst)


# Aumenta o valor em determinados porcentos
def aumentar(value=0, porcento=0, formato=False):
    rst = value + (porcento/100 * value)
    return rst if formato is False else moeda(rst)


# Reduz o valor em determinados porcentos
def reduzir(value=0, porcento=0, formato=False):
    rst = value - (porcento/100 * value)
    return rst if formato is False else moeda(rst)


# formata para valor monetario
def moeda(value=0,moeda="R$"):
    return f"{moeda}{value:>.2f}".replace('.',',')


def resumo(value=0, prct_p=0, prct_n=0):
    print("-"*32)
    print("RESUMO DO VALOR".center(30))
    print("-"*32)
    print(f"Preço analisado: \t{moeda(value)}")
    print(f"Dobro do preço: \t{dobro(value, True)}")
    print(f"Metade do preço: \t{metade(value, True)}")
    print(f"{prct_p}% de aumento: \t{aumentar(value, prct_p, True)}")
    print(f"{prct_n}% de redução: \t{reduzir(value, prct_n, True)}")
    print("-"*32)