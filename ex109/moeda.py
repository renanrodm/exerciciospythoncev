def metade(preço=0, formatação=False):
    res = preço / 2
    if formatação:
        res = moeda(res)
    return res


def dobro(preço=0, formatação=False):
    res = preço * 2
    if formatação:
        res = moeda(res)
    return res


def aumentar(preço=0, taxa=0, formatação=False):
    res = preço * (1 + (taxa / 100))
    if formatação:
        res = moeda(res)
    return res


def diminuir(preço=0, taxa=0, formatação=False):
    res = preço * (1 - (taxa / 100))
    if formatação:
        res = moeda(res)
    return res


def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:.2f}'.replace(".", ",")
