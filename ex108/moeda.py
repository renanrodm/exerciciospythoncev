def metade(n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res


def aumentar(preço, taxa):
    res = preço * (1 + (taxa/100))
    return res


def diminuir(preço, taxa):
    res = preço * (1 - (taxa/100))
    return res
